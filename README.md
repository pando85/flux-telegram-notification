# flux-telegram-notification [![Build Status](https://travis-ci.org/pando85/flux-telegram-notification.svg?branch=master)](https://travis-ci.org/pando85/flux-telegram-notification)  [![](https://images.microbadger.com/badges/image/pando85/flux-telegram-notification.svg)](https://cloud.docker.com/repository/docker/pando85/flux-telegram-notification) [![](https://images.microbadger.com/badges/version/pando85/flux-telegram-notification.svg)](https://cloud.docker.com/repository/docker/pando85/flux-telegram-notification) [![License](https://img.shields.io/github/license/pando85/flux-telegram-notification.svg)](https://github.com/pando85/flux-telegram-notification/blob/master/LICENSE)

Flux notification webhook to forward notifications to Telegram using templates and based in [OpenAPI specs](docs/api/v1/openapi.yaml).

## Config

| *Env* | *Description* | *Default* |
|---------|---------------|-----------|
|`API_SPECS_PATH`| OpenAPI specs path | `docs/api/v1/openapi.yaml` |
|`LOG_LEVEL`| Log level: `[DEBUG, INFO, WARNING, ERROR, CRITICAL]`| `INFO` |
|`TELEGRAM_BOT_TOKEN`| Telegram bot token | `` |
|`TEMPLATE_PATH`| Jinja2 template used to forward messages | | `forwarder/resources/templates/default.j2` |

### Alertmanager

Must set up a [provider](https://toolkit.fluxcd.io/components/notification/provider/#generic-webhook). Replace `{CHAT_ID}` with a desired Telegram chat ID.

```yaml
apiVersion: notification.toolkit.fluxcd.io/v1beta1
kind: Provider
metadata:
  name: flux-telegram-notification
  namespace: flux-system
spec:
  type: generic
  address: http://flux-telegram-notification:8080/v1/event/{CHAT_ID}
```

You can contact with [@myidbot](https://telegram.me/myidbot) to get your current chat ID.

## Deployment

- [Kubernetes example](k8s/example.yml)
