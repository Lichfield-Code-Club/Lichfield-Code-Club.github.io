import facebook
UserToken = 'EAAXAOZBk34wEBANpmtZCFMKjGUCn2DhOyoCziE7WNSOl4tnyo60joj4LyhKOeWHgWx2HxZB0X2rBDmjnQmZB2mfTwaPO7laZBgv7A6Gabqcq5z7ZCwebFGjuryFiURT2I5lB1OK5k06Jk1mliqYBBwr4MMcsJ8tpl0CiOQqXPvDjYDGOrlnwyiqSPpiIuwoTAZD'
AppToken = '1618738431910657|wPrBGEFH1pFXNv_YDA98YH9tQm0'
AppVersion = '2.12'

graph = facebook.GraphAPI(access_token=AppToken, version=AppVersion)
post = graph.get_object(id='post_id',fields='message')
print(post['message'])
