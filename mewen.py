#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MEWEN - Ваш персональный ИИ-ассистент
"""

import sys
import os
from colorama import init, Fore, Style

# Инициализация colorama для Windows
init(autoreset=True)

# Попытка импорта transformers для ИИ
try:
    from transformers import AutoTokenizer, AutoModelForCausalLM
    import torch
    HAS_TRANSFORMERS = True
except ImportError:
    HAS_TRANSFORMERS = False

ASCII_ART = f"""
{Fore.CYAN}███╗   ███╗{Fore.GREEN}██╗    {Fore.YELLOW}██╗    {Fore.RED}██╗
{Fore.CYAN}████╗ ████║{Fore.GREEN}██║    {Fore.YELLOW}██║    {Fore.RED}██║
{Fore.CYAN}██╔████╔██║{Fore.GREEN}██║    {Fore.YELLOW}██║    {Fore.RED}██║
{Fore.CYAN}██║╚██╔╝██║{Fore.GREEN}██║    {Fore.YELLOW}██║    {Fore.RED}██║
{Fore.CYAN}██║ ╚═╝ ██║{Fore.GREEN}███████╗{Fore.YELLOW}██║    {Fore.RED}██║
{Fore.CYAN}╚═╝     ╚═╝{Fore.GREEN}╚══════╝{Fore.YELLOW}╚═╝    {Fore.RED}╚═╝
{Style.BRIGHT}{Fore.WHITE}       Ваш персональный ИИ-ассистент
{Fore.WHITE}       Версия 1.0.0
"""

class MewenAI:
    """Класс для работы ИИ-ассистента"""
    
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.conversation_history = []
        self._load_model()
    
    def _load_model(self):
        """Загружает ИИ-модель"""
        if not HAS_TRANSFORMERS:
            print(f"{Fore.YELLOW}[Инфо] ИИ-модель не загружена. Использую базовые ответы.{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}       Для полноценного ИИ установите: pip install transformers torch{Style.RESET_ALL}\n")
            return
        
        try:
            print(f"{Fore.CYAN}Загрузка ИИ-модели...{Style.RESET_ALL}")
            # Используем небольшую русскоязычную модель
            model_name = "ai-forever/ruGPT-3.5-13B"
            # Для быстрого старта можно использовать меньшую модель:
            # model_name = "sberbank-ai/sber_gpt_mini"
            
            self.tokenizer = AutoTokenizer.from_pretrained("gpt2")  # временное решение
            self.model = AutoModelForCausalLM.from_pretrained("gpt2")
            print(f"{Fore.GREEN}ИИ-модель загружена!{Style.RESET_ALL}\n")
        except Exception as e:
            print(f"{Fore.YELLOW}[Инфо] Не удалось загрузить модель: {e}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}       Использую базовые ответы{Style.RESET_ALL}\n")
    
    def get_response(self, user_input):
        """Получает ответ от ИИ"""
        self.conversation_history.append(user_input)
        
        if self.model and self.tokenizer:
            return self._generate_response(user_input)
        else:
            return self._basic_response(user_input)
    
    def _generate_response(self, text):
        """Генерирует ответ через модель"""
        try:
            inputs = self.tokenizer.encode(text, return_tensors="pt")
            outputs = self.model.generate(
                inputs,
                max_length=100,
                temperature=0.7,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id
            )
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return response
        except Exception as e:
            return f"Ошибка генерации: {e}"
    
    def _basic_response(self, text):
        """Базовые ответы без модели"""
        responses = {
            "привет": "Привет! Как дела?",
            "здравствуй": "Здравствуйте! Чем могу помочь?",
            "как дела": "Отлично! Готов помочь вам.",
            "что ты умеешь": "Пока я учусь, но могу поддержать разговор и ответить на простые вопросы!",
            "кто ты": "Я Mewen - ваш персональный ИИ-ассистент!",
            "помощь": """Доступные команды:
  - помощь: показать это сообщение
  - выход: выйти из программы
  - любой текст: я постараюсь ответить""",
            "спасибо": "Пожалуйста! Обращайтесь 😊",
            "пока": "До свидания! Хорошего дня!",
        }
        
        text_lower = text.lower().strip()
        
        for key, response in responses.items():
            if key in text_lower:
                return response
        
        return f"Вы сказали: '{text}'. Я пока учусь, но скоро смогу отвечать лучше! Задайте другой вопрос."

def print_banner():
    """Выводит приветственный баннер"""
    print(ASCII_ART)
    print(f"{Fore.YELLOW}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Привет! Я Mewen, ваш ИИ-ассистент.{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Напишите 'помощь' для списка команд или 'выход' для выхода.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'='*50}{Style.RESET_ALL}\n")

def chat_loop():
    """Основной цикл чата"""
    print_banner()
    
    # Инициализация ИИ
    ai = MewenAI()
    
    while True:
        try:
            # Ввод пользователя
            user_input = input(f"{Fore.BLUE}Вы: {Style.RESET_ALL}").strip()
            
            if not user_input:
                continue
            
            # Проверка на выход
            if user_input.lower() in ['выход', 'exit', 'quit', 'пока']:
                print(f"\n{Fore.GREEN}До свидания! Было приятно общаться с вами!{Style.RESET_ALL}")
                break
            
            # Получение ответа от ИИ
            response = ai.get_response(user_input)
            
            # Вывод ответа
            print(f"{Fore.MAGENTA}Mewen: {Style.RESET_ALL}{response}\n")
            
        except KeyboardInterrupt:
            print(f"\n\n{Fore.GREEN}До свидания!{Style.RESET_ALL}")
            break
        except Exception as e:
            print(f"{Fore.RED}Ошибка: {e}{Style.RESET_ALL}")

def main():
    """Точка входа"""
    try:
        chat_loop()
    except Exception as e:
        print(f"{Fore.RED}Критическая ошибка: {e}{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()
