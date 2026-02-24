<template>
  <div class="auth">
    <div class="auth__card">
      <div class="auth__top">
        <router-link to="/" class="auth__back">← На главную</router-link>
      </div>

      <h1 class="auth__title">Регистрация</h1>
      <p class="auth__subtitle">Придумайте логин и пароль</p>

      <form class="auth__form" @submit.prevent="onSubmit">
        <input
          v-model="username"
          class="auth__input"
          type="text"
          autocomplete="username"
          placeholder="Логин"
        />

        <input
          v-model="password"
          class="auth__input"
          type="password"
          autocomplete="new-password"
          placeholder="Пароль (минимум 6 символов)"
        />

        <input
          v-model="password2"
          class="auth__input"
          type="password"
          autocomplete="new-password"
          placeholder="Повторите пароль"
        />

        <p v-if="error" class="auth__error">{{ error }}</p>

        <button class="auth__button" type="submit">Зарегистрироваться</button>
      </form>

      <div class="auth__footer">
        Уже есть аккаунт?
        <router-link to="/login">Войти</router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const username = ref('')
const password = ref('')
const password2 = ref('')
const error = ref('')

function onSubmit() {
  error.value = ''

  const u = username.value.trim()
  const p1 = password.value
  const p2 = password2.value

  if (!u || !p1 || !p2) {
    error.value = 'Заполните все поля.'
    return
  }

  if (u.length < 3) {
    error.value = 'Логин должен быть минимум 3 символа.'
    return
  }

  if (p1.length < 6) {
    error.value = 'Пароль должен быть минимум 6 символов.'
    return
  }

  if (p1 !== p2) {
    error.value = 'Пароли не совпадают.'
    return
  }

  // Пока заглушка: считаем, что регистрация успешна
  localStorage.setItem('va_auth', '1')
  localStorage.setItem('va_user', u)

  router.push('/chat')
}
</script>