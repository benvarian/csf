<template>
  <div>
    {{ event }}
  </div>
</template>

<script setup lang="ts">
import { useEventStore } from '@/stores/event'
import { onMounted, ref } from 'vue'
import type { Event } from '@/types/event'
import router from '@/router'
const eventStore = useEventStore()

const event = ref<Event>()
onMounted(async () => {
  event.value = eventStore.getEventById(Number(router.currentRoute.value.params.id))
})
</script>
