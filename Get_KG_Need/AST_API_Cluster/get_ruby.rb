require 'ripper'
require 'json'

def parse_rb_content(rb_content)
  begin
    ast = Ripper.sexp(rb_content)

    api_names = []

    process_node(ast, api_names)

    # Output to standard output
    puts api_names.uniq.to_json

    # Return the parsing result
    return api_names.uniq
  rescue NameError, SyntaxError => e
    puts "Error while parsing Ruby content: #{e.message}"
    return []  # Return an empty array or other appropriate value
  end
end

def process_node(node, api_names)
  case node[0]
  when :def, :defs
    method_name = node[1][1].to_s
    api_names << method_name
  when :command
    method_name = node[1][1].to_s
    api_names << method_name
    process_command_arguments(node[2], api_names)
  when :vcall
    method_name = node[1][1].to_s
    api_names << method_name
  when :call
    process_call_node(node, api_names)
  else
    node.each { |child| process_node(child, api_names) if child.is_a?(Array) }
  end
end

def process_command_arguments(args, api_names)
  args.each do |arg|
    if arg.is_a?(Array)
      process_command_arguments(arg, api_names)
    elsif arg.is_a?(String)
      api_names << arg
    end
  end
end

def process_call_node(node, api_names)
  method_name = node[2][1].to_s
  api_names << method_name
end

if ARGV.length == 1
  rb_content = File.read(ARGV[0])
  parse_rb_content(rb_content)
else
  puts "Usage: ruby get_ruby.rb <path_to_rb_file>"
end
