#
# Тръби в басейн
# Басейн с обем V има две тръби от които се пълни. Всяка тръба има определен дебит (литрите вода минаващи през една
# тръба за един час). Работникът пуска тръбите едновременно и излиза за N часа. Напишете програма, която изкарва
# състоянието на басейна, в момента, когато работникът се върне.
# Вход
# От конзолата се четат четири реда:
# Първият ред съдържа числото V – Обем на басейна в литри – цяло число в интервала [1…10000].
# Вторият ред съдържа числото P1 – дебит на първата тръба за час – цяло число в интервала [1…5000].
# Третият ред съдържа числото P2 – дебит на втората тръба за час– цяло число в интервала [1…5000].
# Четвъртият ред съдържа числото H – часовете които работникът отсъства – реално число в интервала [1.0…24.00]
# Изход
# Да се отпечата на конзолата едно от двете възможни състояния:
# До колко се е запълнил басейна и коя тръба с колко процента е допринесла.
# "The pool is {запълненост на басейна в проценти}% full. Pipe 1: {процент вода от първата тръба}%. Pipe 2: {процент вода от втората тръба}%."
# Aко басейнът се е препълнил – с колко литра е прелял за даденото време.
# "For {часовете, които тръбите са пълнили вода} hours the pool overflows with {литрите вода в повече} liters."

def percentage(part, whole):
    return 100 * float(part) / float(whole)

volume = int(input())
pipe1_debit = int(input())
pipe2_debit = int(input())
hours = float(input())

pipe1_vol = (pipe1_debit * hours)
pipe2_vol = (pipe2_debit * hours)

full = pipe1_vol + pipe2_vol
if full <= volume:
    percent_full = percentage(full, volume)
    pipe1_percent = percentage(pipe1_vol, full)
    pipe2_percent = percentage(pipe2_vol, full)
    print(f"The pool is {percent_full}% full. Pipe 1: {pipe1_percent}%. Pipe 2: {pipe2_percent}%.")
else:
    overfill = full - volume
    print(f"For {hours} hours the pool overflows with {overfill} liters.")
