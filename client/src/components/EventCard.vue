<template>
  <v-hover v-slot="{ isHovering }">
    <v-card class="mx-3 elevation-0" :class="backgroundColour">
      <div>
        <v-card-title
          style="word-break: break-word; overflow-wrap: break-word; white-space: normal"
        >
          <v-row no-gutters>
            <span
              class="font-weight-bold"
              :style="isHovering ? 'cursor: auto' : 'cursor: pointer;'"
              @click="viewEvent"
              >{{ event.name }}</span
            >
            <v-icon
              v-if="user?.teamAdmin && !event.isPublic"
              icon="mdi-pencil"
              @click="openModal"
              size="24"
              class="pl-4 mr-2 mt-1"
              :style="isHovering ? 'cursor: auto' : 'cursor: pointer;'"
            />
            <v-spacer />
            <v-chip
              variant="outlined"
              :class="event.isPublic ? 'text-secondaryBlue' : 'text-secondaryGreen'"
            >
              {{ event.isPublic ? 'Official' : 'Private' }}
            </v-chip>
          </v-row>
        </v-card-title>
        <div @click="viewEvent" :style="isHovering ? 'cursor: auto' : 'cursor: pointer;'">
          <v-card-subtitle class="text-primaryRed font-italic"
            >{{ formatDate(event.startDate) }} - {{ formatDate(event.endDate) }}</v-card-subtitle
          >
          <v-card-text>{{ event.description }}</v-card-text>
        </div>
      </div>
    </v-card>
  </v-hover>
  <v-divider class="mx-4" />
</template>

<script setup lang="ts">
import { useUserStore } from '@/stores/user'
import { type Event } from '../types/event'
import { storeToRefs } from 'pinia'

import formatDate from '../utils/date'

const props = defineProps<{ event: Event; backgroundColour: string }>()
const emit = defineEmits(['edit', 'view'])

const { user } = storeToRefs(useUserStore())

function openModal() {
  emit('edit', props.event.eventId)
}

const viewEvent = () => {
  emit('view', props.event.eventId)
}
</script>

<style>
.v-card-title {
  display: flex;
}
</style>
