import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Моё первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text("Hello world!")

    HISTORY_FILE = "history.txt"

    greeting_history = []

    def load_history():
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    name = line.strip()
                    if name:
                        greeting_history.append(name)
                history_text.value = 'История приветствий:\n' + "\n".join(greeting_history)
                page.update()
        except FileNotFoundError:
            pass 

    def save_history():
        with open(HISTORY_FILE, 'w', encoding='utf-8') as file:
            for name in greeting_history:
                file.write(name + "\n")

    history_text = ft.Text("История приветствий:", size="bodyMedium")



    def on_button_click(_):
        name = name_input.value.strip()
        time = datetime.now().hour
        if name:
            if 6 <= time < 12:
                greeting_text.value = f"Доброе утро, {name}"
                greeting_text.color = "yellow"
            elif 12 <= time < 18:
                greeting_text.value = f"Доброе день, {name}"
                greeting_text.color = "orenge"
            elif 18 <= time < 24:
                greeting_text.value = f"Доброе вечер, {name}"
                greeting_text.color = "red"
            else:
                greeting_text.value = f"Доброе ночи, {name}"
                greeting_text.color = "blue"
            greet_button.text = "Поздороваться снова"
            name_input.value = ""
            greeting_history.append(f"{datetime.now().replace(microsecond=0) }: {name}")
            history_text.value = "История приветсвий:\n" + "\n".join(greeting_history)
            save_history()
        else:
            greeting_text.value = 'Пожалуйста, введите имя ❌'
            
        page.update()


    name_input = ft.TextField(label="Введите имя", autofocus=True,
                                on_submit=on_button_click)

    def clear_history(_):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        page.update()

    def toggle_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        
        page.update()

    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_6, 
                                 tooltip='Сменить тему',
                                 on_click=toggle_theme)

    greet_button = ft.ElevatedButton('Поздороваться', 
                                    on_click=on_button_click,
                                    icon=ft.icons.HANDSHAKE)
    
    clear_button = ft.TextButton("Очистить исорию", icon=ft.icons.DELETE_SWEEP, on_click=clear_history)

    clear_button_2 = ft.IconButton(icon=ft.icons.DELETE,
                                    tooltip='Очистить историю',
                                    on_click=clear_history)

    # page.add(theme_button, greeting_text, name_input, greet_button, history_text, clear_button)
    page.add(ft.Row([theme_button, clear_button, clear_button_2],  alignment=ft.MainAxisAlignment.CENTER),
                    greeting_text,
                    name_input,
                    greet_button,
                    history_text)

ft.app(main)
