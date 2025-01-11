<template>
  <div>
    <h3 class="text-xl text-center mb-8">Strange, yet delicious recipies, give a try!</h3>
    <div class="mb-4">
      <Label for="ingredients-textarea" class="inline-block mb-2">Ingredients</Label>
      <Textarea v-model="formValues['ingredients']" id="ingredients-textarea" placeholder="eg. cheese, butter, garlic powder, salt" class="max-w-lg" />
    </div>
    <div class="mb-10">
      <div class="flex justify-between items-center">
        <Label for="error-threshold-slider" class="inline-block mb-2">Error threshold</Label>
        <Label class="text-primary font-bold inline-block mb-2">{{computedReadableErrorThreshold}}</Label>
      </div>
      <Slider v-model="formValues['error-threshold']" id="error-threshold-slider" :step="0.01"  :min="0" :max="1" />
    </div>
    <Button @click="$emit('send-form', formValues)" size="lg" class="w-full uppercase">Get recipe</Button>
  </div>
</template>
<script setup lang="ts">
import {Button} from "~/components/ui/button";
import {Textarea} from "~/components/ui/textarea";
import {Label} from "~/components/ui/label";
import {Slider} from "~/components/ui/slider";

defineEmits(['send-form'])

const formValues = reactive({
  ingredients: "",
  "error-threshold": [0.25]
})

const computedReadableErrorThreshold = computed(() => {
  if(formValues['error-threshold'][0] === 0) return "0.00"
  if(formValues['error-threshold'][0] === 1) return "1.00"
  return formValues['error-threshold'][0].toString().padEnd(4, "0")
})
</script>