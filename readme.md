# Description

This script in currenct version allows to use shortcuts to process request with OpenAI Service.

## Currently possible options:

1. Stoping script - stop script

- ctrl + alt + 0

2. Translation - translate text from your clipboard (translated text will be appear in your keyboard as translated remember that it may takes a few seconds before translation will be ready).

### Configuration

config.json allows to set one of two types of translation engine - openai and deepl (openai is default and if it wont match to any value it will set translation engine as openai). Engine property has two posssible values: 'deepl' or 'openai'.
To use deepl u have to set deepl api key in your env varaibles, name your variable as "APIKEY-DEEPL".
**WARNING**: Because DeepL doesnt detect target translation language sometimes it may make two request instead of one before it will return answer

```json
{
  "translation": {
    "engine": "deepl"
  }
}
```

### Shortcut:

- ctrl + alt + 1

# Examples

## Example of how much is tokens:

### Embedding-Ada-002

```
A common way to use Chat Completions is to instruct the model to always return a JSON object that makes sense for your use case, by specifying this in the system message. While this does work in some cases, occasionally the models may generate output that does not parse to valid JSON objects.
```

~60 tokens
