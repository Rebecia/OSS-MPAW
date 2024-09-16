# 解析并提取函数调用的脚本
require 'parser/current'
require 'rubygems'
require 'bundler/setup'
$LOAD_PATH.unshift('/Users/zhouxiaoyan/.gem/ruby/2.6.0/gems/unparser-0.6.4/lib')
require 'unparser'
require 'json'

# 读取代码文件并解析为AST
def extract_api_calls_from_file(file_path)
  file_content = File.read(file_path)
  buffer = Parser::Source::Buffer.new(file_path)
  buffer.source = file_content
  parser = Parser::CurrentRuby.new
  ast = parser.parse(buffer)

  # 函数调用节点类型
  api_call_node_types = [:send, :csend]

  # 遍历AST，找到所有的API调用
  def find_api_calls(node, calls = [], api_call_node_types)
    if api_call_node_types.include?(node.type)
      calls << node
    end

    node.children.each do |child|
      if child.is_a?(Parser::AST::Node)
        find_api_calls(child, calls, api_call_node_types)
      end
    end

    calls
  end

  # 提取API调用的名称
  def extract_api_name(node)
    if node.type == :send || node.type == :csend
      method_name = node.children[1]
      receiver = node.children[0]

      if receiver.nil?
        method_name.to_s
      else
        "#{Unparser.unparse(receiver)}.#{method_name}"
      end
    end
  end

  # 获取所有的API调用节点
  api_calls = find_api_calls(ast, [], api_call_node_types)

  # 提取API调用的名称并返回
  api_calls.map { |call| extract_api_name(call) }
end

# 命令行参数处理
if ARGV.length == 1
  api_calls = extract_api_calls_from_file(ARGV[0])
  puts api_calls.to_json # 直接输出 JSON 格式的数据
else
  puts "Usage: ruby get_ruby.rb <path_to_rb_file>"
end







