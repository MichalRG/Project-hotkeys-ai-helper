# Description

This script in currenct version allows to use shortcuts to process request with OpenAI Service.

## Currently possible options:

### 1. Stoping script - stop script

- ctrl + alt + 0

### 2. Translation - translate text from your clipboard (translated text will be appear in your keyboard as translated remember that it may takes a few seconds before translation will be ready).

#### Configuration

config.json allows to set one of two types of translation engine - openai and deepl (openai is default and if it wont match to any value it will set translation engine as openai). Engine property has two posssible values: 'deepl', 'ollama' or 'openai'.

To use [deepl](https://www.deepl.com/pl/your-account/keys) u have to set deepl api key in your env varaibles, name your variable as "APIKEY-DEEPL".
To use OpenAI u have to set openai api key in your env vars, name your variable as "APIKEY-OPENAI".
To use [Ollama](https://ollama.com/) u have to download ollama and run it locally. Currently it use mistral model so to use ollama u have to download and run "mistral" model (TBH it doesnt work in the future I'll try to add configuraiton to manage models from config file, maybe mixtral or llama3 will be able to handle this task).

**WARNING**:

- Because DeepL doesnt detect target translation language sometimes it may make two request instead of one before it will return answer
- Olla for mistral doesnt work for translation it's not able to understand that it has to translate text so it may not work :(

```json
{
  "translation": {
    "engine": "deepl"
  }
}
```

#### Pricing

You can translate up to 500,000 characters per month for free with your api key

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

# Examples

## Example tokens' amount:

### Embedding-Ada-002

```
A common way to use Chat Completions is to instruct the model to always return a JSON object that makes sense for your use case, by specifying this in the system message. While this does work in some cases, occasionally the models may generate output that does not parse to valid JSON objects.
```

~60 tokens
