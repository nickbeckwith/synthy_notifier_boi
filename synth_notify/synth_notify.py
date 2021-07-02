from discord_webhook import DiscordWebhook, DiscordEmbed

DEFAULT_SUCCESS_IMAGE = 'https://i.redd.it/9zdpbppstd171.jpg'
DEFAULT_FAIL_IMAGE = 'https://i.redd.it/kegmnnppupk61.jpg'

def notify(success: int, url: str, message: str, failure: str):
    # create embed object for webhook
    embed = DiscordEmbed()
    if success:
        embed.set_image(url=DEFAULT_SUCCESS_IMAGE)
        content = message
    else:
        embed.set_image(url=DEFAULT_FAIL_IMAGE)
        content = failure if failure is not None else message
    embed.set_timestamp()

    webhook = DiscordWebhook(url=url, content=content)
    webhook.add_embed(embed)
    response = webhook.execute()
    return response.status_code
