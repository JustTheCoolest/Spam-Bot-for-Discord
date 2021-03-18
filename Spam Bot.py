import discord, time
client = discord.Client()

a=''

print ("Please wait for the login confirmation. You can then type !start <message> and !stop in Discord for the spam")

while True:
	t=int(input("\nEnter the amount of time gap (in seconds) between consecutive messages (keep in mind that your device is the server): "))
	if t<0:
		print("Time cannot be negative!")
		continue
	break

while True:
	l=int(input("\nHow many consecutive messages should be permitted from each request? (Enter -1 if you don't want to set a limit) "))
	if l==0:
		print('Invalid input (no use of program if limit is 0), try again')
		continue
	break
c=l-1


@client.event
async def on_ready():
    print('\nWe have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global a,c

    if message.content.startswith('!start'):
        if len(message.content)>6:
        	a=message.content[7:]
        	await message.channel.send(a)
        	c=l-1
        else:
        	await message.channel.send("The syntax for the command is `!start <message to spam>`")
        
    elif message.content.startswith('!stop'):
    	a=''
    
    elif c==0:
    	a=''
    	c=1
    
    elif a!='':
    	time.sleep(t)
    	c-=1
    	await message.channel.send(a)


client.run('Enter your Discord bot token here')
