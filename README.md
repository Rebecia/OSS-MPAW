# OSS-MPAW

## Get_KG：Build Knowledge Graphs and Generate four kinds of Subgrah
- **[Data]** - Our dataset
- **[KG]** - Knowledge Graph
- **[SubGraph]** - All Subgraphs(unclassified) and Four Subgraphs

## Get_KG_Need: Obtain the information required to establish KGs

### AST_API_Cluster：Extract source code APIs through AST、 Embed and Cluster
- **[sourcecode_cluster]** - Get APIs、Embed and CLuster
- **[get_ruby]** - Get .rb APIs(Python doesn‘t include libraries that can directly process Ruby files)

### Get_Report：Get the report that the package to appear in it
- **[get_report_name]** - Crawl URLs in 'report.xlsx' and determine if the package appears within it
- **[report]** - Our reports dataset

### Get_Other：Get numbers of downloads and evolutions of packages
- **[sort_evolution]** - Sort packages within each group according to their release time and obtain the evolutions
- **[get_download_num_3OSS]** - Crawl the number of downloads for packages of 3 OSS
- **[active_time]** - Get the active time of each group
- **[Sum]** - Our information dataset of DeG、SG and CG(include evolution、download nnumbers and so on)
<!-- ## Resources

- **[Embedded App SDK Docs](https://discord.com/developers/docs/developer-tools/embedded-app-sdk)** - Get familiar with the Embedded App SDK
- **[Activity Examples](/examples/)** - Explore examples of Discord Activities
- **[Technical chat on Discord](https://discord.com/invite/discord-developers)** - Join us and other devs at DDevs at `#activities-dev-help`

## Installing this package

```shell
npm install @discord/embedded-app-sdk
```

## Usage

To use the SDK, import it into your project and construct a new instance of the DiscordSDK class.

Below is a minimal example of setting up the SDK.
Visit [/examples/discord-activity-starter](/examples/discord-activity-starter/README.md) for a complete example application. See more info on environment variables (`YOUR_OAUTH2_CLIENT_ID`, etc...) [here](https://discord.com/developers/docs/activities/building-an-activity#find-your-oauth2-credentials).

```typescript
import {DiscordSDK} from '@discord/embedded-app-sdk';
const discordSdk = new DiscordSDK(YOUR_OAUTH2_CLIENT_ID);

async function setup() {
  // Wait for READY payload from the discord client
  await discordSdk.ready();

  // Pop open the OAuth permission modal and request for access to scopes listed in scope array below
  const {code} = await discordSdk.commands.authorize({
    client_id: YOUR_OAUTH2_CLIENT_ID,
    response_type: 'code',
    state: '',
    prompt: 'none',
    scope: ['identify'],
  });

  // Retrieve an access_token from your application's server
  const response = await fetch('/api/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      code,
    }),
  });
  const {access_token} = await response.json();

  // Authenticate with Discord client (using the access_token)
  auth = await discordSdk.commands.authenticate({
    access_token,
  });
}
```

## SDK development

Developing a new feature or patching a bug on the SDK? Check out [this guide](/docs/local-sdk-development.md) to learn how to set up your local dev environment.

## Discord Developer Terms of Service & Developer Policy

Please note that while this SDK is licensed under the MIT License, the [Discord Developer Terms of Service](https://discord.com/developers/docs/policies-and-agreements/developer-terms-of-service) and [Discord Developer Policy](https://discord.com/developers/docs/policies-and-agreements/developer-policy) otherwise still apply to you and the applications you develop utilizing this SDK. -->