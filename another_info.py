from parse_func import parser, parser_io






# from 0 to 9
async def all_comments(num):
    soup = await parser('https://baza-gai.com.ua')
    comments = soup.find_all('tr', class_='pt-3 pb-3')
    finall_comment = comments[num].text.strip()
    finall_comment = finall_comment.splitlines()
    out = f'Номер: <code>{finall_comment[4].strip()}</code>\nАвтор: {finall_comment[15].strip()}\nВідгук: \n{finall_comment[20].strip()}\n{finall_comment[23].strip()}'
    number = f'{finall_comment[4].strip()}'
    number = number.replace(' ', '')
    return out, number

