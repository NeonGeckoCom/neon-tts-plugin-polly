# NeonAI Amazon Polly TTS Plugin
[Mycroft](https://mycroft-ai.gitbook.io/docs/mycroft-technologies/mycroft-core/plugins) compatible
TTS Plugin for Amazon Polly Text-to-Speech.

# Configuration:
A credential should be saved at: `~/.aws/credentials`.
Credentials may alternatively be included in the tts configuration as shown below.

```yaml
tts:
    module: amazon_polly
    amazon_polly:
      aws_access_key_id: ''
      aws_secret_access_key: ''
      region: us-west-2
```