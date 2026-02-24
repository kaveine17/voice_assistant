<template>
  <div class="auth">
    <div class="auth__card">
      <div class="auth__top">
        <router-link to="/" class="auth__back">← На главную</router-link>
      </div>

      <h1 class="auth__title">Вход</h1>
      <p class="auth__subtitle">Введите логин и пароль</p>

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
          autocomplete="current-password"
          placeholder="Пароль"
        />

        <p v-if="error" class="auth__error">{{ error }}</p>

        <button class="auth__button" type="submit">Войти</button>
      </form>

      <div class="auth__footer">
        Нет аккаунта?
        <router-link to="/register">Зарегистрироваться</router-link>
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
const error = ref('')

function onSubmit() {
  error.value = ''

  const u = username.value.trim()
  const p = password.value.trim()

  if (!u || !p) {
    error.value = 'Заполните логин и пароль.'
    return
  }

  // Пока заглушка авторизации
  localStorage.setItem('va_auth', '1')
  localStorage.setItem('va_user', u)

  router.push('/chat')
}
</script>