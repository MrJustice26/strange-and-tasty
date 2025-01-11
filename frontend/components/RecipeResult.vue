<template>
  <div>
    <div class="mb-4">
      <h3 class="text-3xl font-medium mb-2">{{sample.title}}</h3>
      <Button v-if="sample.link" variant="link" class="pl-0" as-child>
        <a :href="sample.source">
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

defineEmits(["display-form"])

const sample = {
	id: 2,
	title: "Creamy Corn",
	ingredients: "2 (16 oz.) pkg. frozen corn, 1 (8 oz.) pkg. cream cheese, cubed, 1/3 c. butter, cubed, 1/2 tsp. garlic powder, 1/2 tsp. salt, 1/4 tsp. pepper",
	directions: "In a slow cooker, combine all ingredients. Cover and cook on low for 4 hours or until heated through and cheese is melted. Stir well before serving. Yields 6 servings.",
	link: "www.cookbooks.com/Recipe-Details.aspx?id=10570",
	source: "Gathered",
	NER: "frozen corn, cream cheese, butter, garlic powder, salt, pepper"
}

const ingredientsArray = computed(() => sample.ingredients.split(", "))
const directionsArray = computed(() => sample.directions.split(". "))
</script>