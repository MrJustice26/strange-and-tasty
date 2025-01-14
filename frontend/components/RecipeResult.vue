<template>
  <div>
    <div class="mb-4">
      <h3 class="text-3xl font-medium mb-2">{{recipe.title}}</h3>
      <Button v-if="recipe?.link" variant="link" class="pl-0" as-child>
        <a :href="`https://${recipe.link}`" target="_blank">
          Recipe link
        </a>
      </Button>
    </div>
    <div class="mb-4">
      <h4 class="text-2xl mb-2">Ingredients</h4>
      <ul class="list-disc pl-5">
        <li v-for="ingredient in ingredientsArray" :key="ingredient">
          {{ingredient}}
        </li>
      </ul>
    </div>
    <div class="mb-4">
      <h4 class="text-2xl mb-2">Directions</h4>
      <ul class="list-decimal pl-5">
        <li v-for="direction in directionsArray" :key="direction">
          {{direction}}
        </li>
      </ul>
    </div>
    <Button class="w-full" size="lg" @click="$emit('display-form')">Get another recipe</Button>
  </div>
</template>

<script setup lang="ts">

import type {Recipe} from "~/types/recipe";

defineEmits(["display-form"])

const props = defineProps<{
  recipe: Recipe
}>()

const ingredientsArray = computed(() => props.recipe.ingredients.split(", "))
const directionsArray = computed(() => props.recipe.directions.split(". "))
</script>