<template>
  <div class="page">
    <div class="card">
      <div class="badge">Дипломный проект</div>

      <h1 class="title">🎙 Интеллектуальный ассистент</h1>
      <p class="subtitle">
        Веб-приложение с голосовым управлением и личным кабинетом (логин/пароль)
      </p>

      <div class="actions">
        <router-link to="/login" class="btn btn--primary">Войти</router-link>
        <router-link to="/register" class="btn btn--ghost">Регистрация</router-link>
      </div>

      <div class="meta">
        <span>Vue 3</span>
        <span>FastAPI</span>
        <span>PostgreSQL</span>
        <span>Web Speech API</span>
      </div>
    </div>
  </div>
</template>