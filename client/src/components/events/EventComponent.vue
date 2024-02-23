<template>
  <v-container>
    <v-row class="mx-6" :fullscreen="mobile">
      <v-row align="center" class="my-2 px-5">
        <v-col align="center">
          <h1>{{ event?.name }}</h1>
        </v-col>
      </v-row>
    </v-row>

    <v-divider />

    <!-- Invite Code -->
    <v-row align="center" class="my-2">
      <v-col>
        <h2 v-if="!isUserSignedUp">Sign Up</h2>
        <h2 v-else>Joined</h2>
        <!-- <p class="invite-code">{{ teamData.invite_code }}</p> -->
      </v-col>
      <v-tooltip location="end">
        <template v-slot:activator="{ props }">
          <!-- if the user is signed up to event have different logo -->
          <v-icon @click="copyInviteCode" v-bind="props" :class="{
            'mdi mdi-account-plus-outline px-10':
              !isUserSignedUp, 'mdi mdi-account-check-outline px-10': isUserSignedUp
          }" size="32px" />
        </template>
        <span v-if="!isUserSignedUp">Join Event</span>
        <span v-else>Already Signed Up</span>
      </v-tooltip>
    </v-row>
    <v-divider />

    <!-- Description -->
    <v-container class="pa-0">
      <v-row id="pointer-cursor" class="my-2">
        <v-col @click="isDescVisible = !isDescVisible">
          <h2>Description</h2>
        </v-col>
        <v-icon v-if="isDescVisible" icon="mdi mdi-chevron-down" @click="isDescVisible = !isDescVisible" class="px-10"
          size="50px" />
        <v-icon v-else icon="mdi mdi-chevron-right" @click="isDescVisible = !isDescVisible" class="px-10" size="50px" />
      </v-row>
      <v-row v-if="isDescVisible" class="mt-n4 mb-2">
        <v-col>
          <p>{{ event?.description }}</p>
        </v-col>
      </v-row>
    </v-container>
    <v-divider></v-divider>

    <!-- Daily Kilometres -->
    <v-container class="pa-0">
      <v-row align="start" id="pointer-cursor" class="my-2">
        <v-col @click="isDailyKmsVisible = !isDailyKmsVisible">
          <h2>Daily KMs</h2>
        </v-col>
        <v-icon v-if="isDailyKmsVisible" @click="isDailyKmsVisible = !isDailyKmsVisible" icon="mdi mdi-chevron-down"
          size="50px" class="px-10" />
        <v-icon v-else @click="isDailyKmsVisible = !isDailyKmsVisible" icon="mdi mdi-chevron-right" size="50px"
          class="px-10" />
      </v-row>
      <v-row v-if="isDailyKmsVisible" class="mt-n4 mb-2">
        <v-col>
          <!-- ! add in the data for the event -->
          <p>data</p>
          <!-- <MileageGraph :dataPoints="mileageStore.mileageByTeam" /> -->
        </v-col>
      </v-row>
    </v-container>
    <v-divider />

    <!-- Leaderboard -->
    <v-container class="pa-0">
      <v-row align="start" @click="isLeaderboardVisible = !isLeaderboardVisible" id="pointer-cursor" class="my-2">
        <v-col>
          <h2>Leaderboard</h2>
        </v-col>
        <v-icon v-if="isLeaderboardVisible" icon="mdi mdi-chevron-down" size="50px" class="px-10" />
        <v-icon v-else icon="mdi mdi-chevron-right" size="50px" class="px-10" />
      </v-row>
      <div v-if="isLeaderboardVisible" class="mx-12">
        <v-table fixed-header class="py-2">
          <thead>
            <tr>
              <th id="placeColumn" class="text-right">Place</th>
              <th id="nameColumn" class="text-left">Name</th>
              <th id="distanceColumn" class="text-right">Distance</th>
            </tr>
          </thead>
          <tbody>
            <!-- <tr v-for="entry in teamData.leaderboard?.leaderboard" :key="entry.rank">
                <td v-if="entry.rank < 4" class="text-right text-subtitle-1">
                  <v-icon icon="mdi-trophy" size="25px" :class="getTrophyColour(entry.rank)" />
                  <span>{{ entry.rank }}</span>
                </td>
                <td v-if="entry.rank > 3" class="text-right text-subtitle-1">
                  <span>{{ entry.rank }}</span>
                </td>
                <td class="text-subtitle-1">
                  <span>{{ entry.username }}</span>
                </td>
                <td class="text-right text-subtitle-1">
                  {{ Math.round(entry.totalMileage * 100) / 100 }}
                </td>
              </tr> -->
          </tbody>
        </v-table>
      </div>
    </v-container>
    <v-divider />
  </v-container>
</template>

<script setup lang="ts">
import { useEventStore } from '@/stores/event'
import { useUserStore } from '@/stores/user'
import { onMounted, ref } from 'vue'
import type { Event } from '@/types/event'
import type { UsersEvents } from '@/types/user'
import router from '@/router'
import { useDisplay } from 'vuetify'
const { mobile } = useDisplay()

const eventStore = useEventStore();
const userStore = useUserStore();
const isDescVisible = ref(false)
const isDailyKmsVisible = ref(false)
const isLeaderboardVisible = ref(false)
const isUserSignedUp = ref(false);

const event = ref<Event>()
onMounted(async () => {
  if (eventStore.events.length < 1) {
    await eventStore.getEvents()
  }
  event.value = eventStore.getEventById(Number(router.currentRoute.value.params.id))
  checkIfUserIsSignedUp();

})

const checkIfUserIsSignedUp = () => {
  if (userStore.user?.events === null) return;
  for (const [key, value] of Object.entries(userStore.user?.events as UsersEvents)) {
    console.log(value);

    if (event.value?.eventId === value) {
      isUserSignedUp.value = true;
    }

  }
}
</script>
