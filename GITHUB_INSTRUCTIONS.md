# 📋 Инструкция по загрузке Mewen на GitHub

## Шаг 1: Создай аккаунт на GitHub (если нет)

1. Зайди на https://github.com
2. Нажми **Sign up**
3. Заполни форму и подтверди email

---

## Шаг 2: Создай новый репозиторий

1. Войди на GitHub
2. Нажми **+** в правом верхнем углу → **New repository**
3. Заполни:
   - **Repository name:** `mewen`
   - **Description:** `Mewen - Ваш персональный ИИ-ассистент в консоли`
   - **Public** (чтобы другие могли скачать)
   - ❌ НЕ ставь галочку "Add README"
4. Нажми **Create repository**

---

## Шаг 3: Установи Git (если не установлен)

1. Скачай с https://git-scm.com/download/win
2. Установи, нажимая "Next" (настройки по умолчанию)
3. Перезапусти командную строку

---

## Шаг 4: Настрой Git

Открой командную строку и выполни:

```bash
git config --global user.name "ТВОЙ_USERNAME"
git config --global user.email "твой@email.com"
```

---

## Шаг 5: Загрузи файлы Mewen

### Вариант А: Через командную строку (рекомендуется)

```bash
# Перейди в папку с проектом
cd E:\mewen

# Инициализируй Git
git init

# Добавь все файлы
git add .

# Создай первый коммит
git commit -m "Initial commit: Mewen AI assistant v1.0"

# Переименуй ветку в main
git branch -M main

# Добавь ссылку на GitHub (замени YOUR_USERNAME на свой логин)
git remote add origin https://github.com/YOUR_USERNAME/mewen.git

# Загрузи на GitHub
git push -u origin main
```

### Вариант Б: Через GitHub Desktop (проще)

1. Скачай https://desktop.github.com
2. Установи и войди в аккаунт
3. **File** → **Add Local Repository** → выбери `E:\mewen`
4. Нажми **Publish repository**
5. Выбери существующий репозиторий `mewen`

---

## Шаг 6: Проверь загрузку

1. Зайди на https://github.com/YOUR_USERNAME/mewen
2. Ты должен увидеть все файлы проекта

---

## Шаг 7: Обнови ссылку установки

После загрузки, команда для установки будет:

```bash
curl -fsSL -o %TEMP%\install-mewen.bat https://raw.githubusercontent.com/YOUR_USERNAME/mewen/main/install-mewen.bat && %TEMP%\install-mewen.bat
```

**Замени `YOUR_USERNAME` на свой GitHub логин!**

---

## 🔄 Как обновлять проект

Когда внесёшь изменения в код:

```bash
cd E:\mewen
git add .
git commit -m "Описание изменений"
git push
```

---

## ❌ Возможные проблемы

### Проблема: "Permission denied"
**Решение:** Убедись, что указал правильный username в ссылке

### Проблема: "Nothing to commit"
**Решение:** Файлы уже загружены, всё ок!

### Проблема: Git не найден
**Решение:** Установи Git с https://git-scm.com/download/win

---

## ✅ Готово!

Теперь любой может установить Mewen одной командой:

```bash
curl -fsSL -o %TEMP%\install-mewen.bat https://raw.githubusercontent.com/YOUR_USERNAME/mewen/main/install-mewen.bat && %TEMP%\install-mewen.bat
```

А запустить командой:
```bash
Mewen
```

---

**Нужна помощь?** Создай Issue в репозитории!
