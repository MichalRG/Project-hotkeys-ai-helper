# Description

This script in currenct version allows to use shortcuts to process request with OpenAI Service.

## Currently possible options:

### 1. Stoping script - stop script

- ctrl + alt + 0

### 2. Translation - translate text from your clipboard (translated text will be appear in your keyboard as translated remember that it may takes a few seconds before translation will be ready).

#### Configuration

config.json allows to set one of four types of translation engine - openai/ ollama/ anthropic and deepl (openai is default and if it wont match to any value it will set translation engine as openai). Engine property has four posssible values: 'deepl', 'ollama', 'anthropic' or 'openai'.

To use [deepl](https://www.deepl.com/pl/your-account/keys) u have to set deepl api key in your env varaibles, name your variable as "APIKEY-DEEPL".
To use OpenAI u have to set openai api key in your env vars, name your variable as "APIKEY-OPENAI".
To use [Ollama](https://ollama.com/) u have to download ollama and run it locally. Currently it use mistral model so to use ollama u have to download and run "mistral" model (TBH it doesnt work in the future I'll try to add configuraiton to manage models from config file, maybe mixtral or llama3 will be able to handle this task).

Command to run ollama mistral model locally

```bash
ollama run mistral
```

**WARNING**:

- Because DeepL doesnt detect target translation language sometimes it may make two request instead of one before it will return answer
- Olla mistral work very poorly for translation it's not able to understand that it has to translate text so it may not work :(

Example of configuration in config.json:

```json
{
  "translation": {
    "engine": "deepl",
    "model": "gpt-4o"
  }
}
```

#### Pricing

You can translate up to 500,000 characters per month for free with your api key (deepl)

#### Shortcut:

- ctrl + alt + 1

### 3. Wolfram Alpha request

#### Configuration

To use [Wolfram alpha](https://products.wolframalpha.com/api/documentation) u have to set wolfram api key in your env vars, name your variable as "APIKEY-WOLFRAM-ALPHA". When you will generate wolfram api key choose Full Results API. Aim of Wolfram in this copilot is to mainly calcualte, so sometimes it may not answer your question and it will return "Wolfram result not found in XML or unavailable".

**WARNING** Sometimes wolfram doesnt return response immidietly especially if it finds task as demanding. So the result from time to time may appear after few seconds you perform action.

#### Pricing

Wolfram API allows to make 2000 request per month for free ;)

#### Possibilites

- it calcualtes values e.g.

```plaintext
7*7 = returns => 47
1742+548*6/3 = returns => 2838
3472+5825 = return => 9297
```

- some statistics operation e.g.

```plaintext
mean {21.3, 38.4, 12.7, 41.6} = returns => 28.5
```

- simple equation (program is not able to parse properly answer for e.g. differential equations yet ;))

```
solve a x^2 + b x + c = 0 for x = returns => x = -(sqrt(b^2 - 4 a c) + b)/(2 a) and a!=0
```

- it's able to answer question about countries like population, capitals

```plaintext
Population of Poland = returns => "41 mln (est. 2023)"
Capital of California = returns => "Sacramento, California, United States"
```

- it's able to answer some countries-related questions e.g.

```plaintext
Who is the president of Japan? = returns => "Fumio Kishida (from 2021-10-04 to present)"
Who is the king of UK? = returns => "King Charles III (from 2022-09-08 to present)"
```

- it also has posssiblites to process different task which I haven't describe or they are not handle in logic yet :) (e.g. Wolfram is able to return information about materials but the program is not able to parse result properly and it wont return any sensible response).

#### Shortcut:

- ctrl + alt + 2

### 4. Gramma

#### Configuration

config.json allows to set one of mnay types of general question engine - openai, anthropic and ollama (openai is default and if it wont match to any value it will set translation engine as openai). Engine property has three posssible values: 'anthropic', 'ollama' or 'openai'.

To use OpenAI u have to set openai api key in your env vars, name your variable as "APIKEY-OPENAI".
To use [Ollama](https://ollama.com/) u have to download ollama and run it locally.
To use Anthropic models u have to set anthropic api key in your env vars, name your variable as "APIKEY-ANTHROPIC".

Command to run ollama mistral model locally

Example of configuration in config.json:

```json
{
  "gramma": {
    "engine": "openai",
    "model": "gpt-4o"
  }
}

{
  "general_question": {
    "engine": "anthropic",
    "model": "claude-3-opus-20240229"
  }
}
```

#### Shortcut:

- ctrl + alt + 3

# Models

The code allows to integrate with OpenAI API, Anthropic API, Ollama model in background.

### 5. General question

#### Configuration

config.json allows to set one of two types of general question engine - openai, anthropic and ollama (openai is default and if it wont match to any value it will set translation engine as openai). Engine property has three posssible values: 'anthropic', 'ollama' or 'openai'.

To use OpenAI u have to set openai api key in your env vars, name your variable as "APIKEY-OPENAI".
To use [Ollama](https://ollama.com/) u have to download ollama and run it locally.

Command to run ollama mistral model locally

```bash
ollama run mistral
```

Example of configuration in config.json:

```json
{
  "general_question": {
    "engine": "openai",
    "model": "gpt-4o"
  }
}

{
  "general_question": {
    "engine": "anthropic",
    "model": "claude-3-opus-20240229"
  }
}
```

#### Shortcut:

- ctrl + alt + 4

# Models

The code allows to integrate with OpenAI API, Anthropic API, Ollama model in background.

1. If u work with openai, u can set such values for models like: "gpt-3.5-turbo" (quick and cheap), "gpt-4" (efficient but most expensive), "gpt-4o" (cheper then gpt-4 seems to be equally good or even better then gpt-4)
2. If u work wiht Ollama u can install localy models and run them. Example of models: "mistral" (small, quite stupid, but respond quite quick and doesnt take too much place), "mixtral" (better version of mistral much bigger)
3. If u work with Anthropic u can set models like: "claude-3-haiku-20240307" (fastest and most compact model, designed for near-instant responsiveness, the chepaest from Claude 3 family), claude-3-sonnet-20240229 (most balanced model between intelligence and speed, mid-tier price), claude-3-opus-20240229 (the most powerful model, high quality, performance may not be the best, the most expensive to use). There is also legacy models like "Claud-2.1" it should also work but lower models may not be handle properly (e.g. they don't handle system prompts there is lack of logic to handle such scenario).

# Examples

## Example tokens' amount:

### Embedding-Ada-002

```
A common way to use Chat Completions is to instruct the model to always return a JSON object that makes sense for your use case, by specifying this in the system message. While this does work in some cases, occasionally the models may generate output that does not parse to valid JSON objects.
```

~60 tokens

# TODO

1. Translate part of script for ollama configuration is adjust only for mistral. It should be more generic I have to rewrite logic for passing prompt and adjust it to user's ollama model.
