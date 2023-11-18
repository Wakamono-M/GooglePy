import tkinter as tk
import webbrowser
from googlesearch import search

def search_google():
    user_query = entry.get()

    try:
        # Используем googlesearch для выполнения поиска
        results = list(search(user_query, num=5, stop=5, pause=2, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"))

        # Открываем страницу с результатами поиска Google в браузере
        search_url = f"https://www.google.com/search?q={'+'.join(user_query.split())}"
        webbrowser.open(search_url)
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Произошла ошибка: {str(e)}")

# Создаем основное окно
app = tk.Tk()
app.title("Гугл 0.1")

# Устанавливаем иконку приложения
app.iconbitmap('wokamone.ico')  # Замените 'path/to/your/icon.ico' на реальный путь к вашей иконке

# Создаем и размещаем виджеты в окне
label = tk.Label(app, text="Введите ваш запрос пожалуйста:")
label.pack(pady=10)

entry = tk.Entry(app, width=50)
entry.pack(pady=10)

search_button = tk.Button(app, text="Обработка", command=search_google)
search_button.pack(pady=10)

result_text = tk.Text(app, height=10, width=70)
result_text.pack(pady=10)

# Запускаем главный цикл событий
app.mainloop()
