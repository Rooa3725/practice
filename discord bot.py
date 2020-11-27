import discord
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready(): # 봇이 실행 준비가 되었을 때 행동할 것
    print('짜잔! 이몸 등장!')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('상시 대기'))

@client.event
async def on_message(message): # 입력되는 메세지에서 찾기
    if message.content.startswith('!ping'): # 만약 메세지가 '!ping'으로 시작된다면
        await message.channel.send('pong') # 클라이언트는 메세지가 올라온 채널에 'pong'을 보냅니다.

    if message.content.startswith('!pong'):
        await message.channel.send('ping!')

    if message.content.startswith('!안녕'):
        await message.channel.send('안녕하세요!')
    
    if message.content.startswith('!ㅎㅇ'):
        await message.channel.send('안녕하세요!')

    if message.content.startswith('!도와줘'):
        await message.channel.send('무슨일이세요?')

    if message.content.startswith('화장실'):
        await message.channel.send('쾌변하세요!')

    if message.content.startswith('장실'):
        await message.channel.send('쾌변하세요!')

    if message.content.startswith('장실점'):
        await message.channel.send('쾌변하세요!')

    if message.content.startswith('장실 점'):
        await message.channel.send('쾌변하세요!')

    if message.content.startswith('!왜 두번 말해'):
        await message.channel.send('제가 두번 말했다구요?')

    if message.content.startswith('ㅅㅂ'):
        await message.channel.send('왜 욕을 하세요...')

    if message.content.startswith('ㅗ'):
        await message.channel.send('욕 하지 말아주세요 ㅠ...')
    
    if message.content.startswith('!clear'):
        await message.channel.purge(limit=10)

    if message.content.startswith('!nuclear'):
        await message.channel.purge(limit=10000)

    '''
    on_message에서 또다른 명령어 추가를 위해
    if message.content.startswith를 추가해야하는데, elif가 아닌 개별 if를 사용하는 것을 추천합니다.
    '''



client.run('Nzc2NjMzMjE2ODM1NjQ5NTY2.X63uDA.gT9AjSn4qVE7KDwNtRsdBHMMg48')