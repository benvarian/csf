<script setup lang="ts">
import NavbarComponents from './components/NavbarComponents.vue'
import ReloadPWA from './components/ReloadPWA.vue'
import { RouterView } from 'vue-router'
</script>

<template>
  <ReloadPWA />
  <NavbarComponents />
  <RouterView />
  <notifications
    classes="csf-notification"
    position="bottom right"
    width="350px"
    :closeOnClick="true"
  />
</template>

<style>
body {
  padding-top: 64px;
}

@font-face {
  font-family: 'Hackney';
  src: local('Hackney'), url('./assets/fonts/Hackney-Vector.ttf') format('truetype');
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Black italic.otf') format('opentype');
  font-weight: 900;
  font-style: italic;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Black.otf') format('opentype');
  font-weight: 900;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Bold italic.otf') format('opentype');
  font-weight: 700;
  font-style: italic;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Bold.otf') format('opentype');
  font-weight: 700;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Extra Light italic.otf') format('opentype');
  font-weight: 200;
  font-style: italic;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Extra Light.otf') format('opentype');
  font-weight: 200;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Light italic.otf') format('opentype');
  font-weight: 300;
  font-style: italic;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Light.otf') format('opentype');
  font-weight: 300;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Medium italic.otf') format('opentype');
  font-weight: 500;
  font-style: italic;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Medium.otf') format('opentype');
  font-weight: 500;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Regular italic.otf') format('opentype');
  font-weight: 400;
  font-style: italic;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Regular.otf') format('opentype');
  font-weight: 400;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Semi Bold italic.otf') format('opentype');
  font-weight: 600;
  font-style: italic;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Semi Bold.otf') format('opentype');
  font-weight: 600;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Ultra Light italic.otf') format('opentype');
  font-weight: 100;
  font-style: italic;
}

@font-face {
  font-family: 'Sofia Pro';
  src: local('Sofia Pro'),
    url('./assets/fonts/Mostardesign - Sofia Pro Ultra Light.otf') format('opentype');
  font-weight: 100;
}

.csf-notification {
  padding: 2%;
  margin-bottom: 3%;
  margin-right: 3%;
  font-size: 14px;
  color: #ffffff;
  background: #44a4fc;
  text-align: center !important;
}

.csf-notification.success {
  background: rgb(0, 157, 79);
}

.csf-notification.error {
  background: rgb(237, 28, 36);
}
</style>
