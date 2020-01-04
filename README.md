# Emby Webhook Proxy
Emby's webhooks come in as multi-part requests with a single part being a json payload. 

For some reason this breaks node-red (my primary use-case) so to fix this I am proxying my requests through this docker container instead

## Usage
`docker run -d -p 5000:5000 -e FORWARD_URL=https://nodered.domain.com/webhook bigtoach/emby-webhook-proxy:latest`
