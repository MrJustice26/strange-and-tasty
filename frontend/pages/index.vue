<template>
  <div class="flex items-center justify-center mt-20">
    <h1 class="text-5xl font-bold bg-gradient-to-r from-blue-600 via-green-500 to-indigo-400 inline-block text-transparent bg-clip-text py-2">✨Strange & Tasty✨</h1>
  </div>
  <div class="container max-w-xl flex justify-center flex-col h-[calc(100vh-144px)]">
    <Transition
      mode="out-in"
      enter-active-class="duration-300 ease-out opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="duration-200 ease-in"
      leave-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <MainForm @send-form="sendForm" v-if="displayState === DISPLAY_STATE.DISPLAY_FORM" />
      <div v-else-if="displayState === DISPLAY_STATE.DISPLAY_LOADER" class='flex space-x-2 justify-center items-center'>
        <div class='h-8 w-8 bg-primary rounded-full animate-bounce [animation-delay:-0.3s]'></div>
        <div class='h-8 w-8 bg-primary rounded-full animate-bounce [animation-delay:-0.15s]'></div>
        <div class='h-8 w-8 bg-primary rounded-full animate-bounce'></div>
      </div>
      <div v-else-if="displayState === DISPLAY_STATE.DISPLAY_RESULTS">
        <RecipeResult @display-form="displayState = DISPLAY_STATE.DISPLAY_FORM" />
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
enum DISPLAY_STATE {
  DISPLAY_FORM,
  DISPLAY_LOADER,
  DISPLAY_RESULTS
}

import MainForm from "~/components/MainForm.vue";
import type {Reactive} from "vue";

const displayState = ref<DISPLAY_STATE>(DISPLAY_STATE.DISPLAY_FORM);

const sendForm = (formValues: Reactive<{
  ingredients: string,
  "error-threshold": [number]
}>) => {
  const formattedIngredients = formValues['ingredients'].replaceAll("\n", ", ")
  const payload = {
    ingredients: formattedIngredients,
    "error-threshold": formValues['error-threshold'][0]
  }
  displayState.value = DISPLAY_STATE.DISPLAY_LOADER;
  setTimeout(() => {
    displayState.value = DISPLAY_STATE.DISPLAY_RESULTS;
  }, 3000)
}

</script>