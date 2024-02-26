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
    <!-- change the mileageStore thing to the events mileage -->
    <v-row class="ma-0 px-4 pb-0 pt-0" align="center">
      <v-col>
        <v-card variant="flat" class="pb-1">
          <v-container class="pa-0" fluid>
            <v-row class="ma-0">
              <v-row align="center" class="my-1">
                <v-icon :class="['mdi', 'ml-2', method]" size="52" color="#2c3d4f" />
                <v-col class="pb-0">
                  <v-chip color="green" class="rounded text-h5"
                    >{{ Math.round((event?.totalMileage as number) * 100) / 100 }} KM</v-chip
                  >
                  <h3>TOTAL</h3>
                </v-col>
              </v-row>

              <v-spacer />
              <v-col cols="auto">
                <v-btn
                  variant="elevated"
                  elevated="2"
                  :ripple="true"
                  icon="mdi-plus"
                  color="primaryRed"
                  @click="dialog = true"
                />
                <MileageModal v-model="dialog" @handle-submit="updateEvent" />
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-col>
    </v-row>

    <v-divider />

    <!-- Invite Code -->
    <v-row align="center" class="my-2">
      <v-col>
        <h2 v-if="!isUserSignedUp">Sign Up</h2>
        <h2 v-else>Joined</h2>
      </v-col>
      <v-tooltip location="end">
        <template v-slot:activator="{ props }">
          <v-icon
            v-if="isUserSignedUp"
            v-bind="props"
            class="mdi mdi-account-check-outline px-10"
            size="32px"
          />
          <v-icon
            v-if="!isUserSignedUp"
            @click="signUpEvent"
            v-bind="props"
            class="mdi mdi-account-plus-outline px-10"
            size="32px"
          />
        </template>
        <span v-if="!isUserSignedUp">Join Event</span>
        <span v-if="isUserSignedUp">Already Signed Up</span>
      </v-tooltip>
    </v-row>
    <v-divider />

    <!-- Description -->
    <v-container class="pa-0">
      <v-row id="pointer-cursor" class="my-2">
        <v-col @click="isDescVisible = !isDescVisible">
          <h2>Description</h2>
        </v-col>
        <v-icon
          v-if="isDescVisible"
          icon="mdi mdi-chevron-down"
          @click="isDescVisible = !isDescVisible"
          class="px-10"
          size="50px"
        />
        <v-icon
          v-else
          icon="mdi mdi-chevron-right"
          @click="isDescVisible = !isDescVisible"
          class="px-10"
          size="50px"
        />
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
        <v-icon
          v-if="isDailyKmsVisible"
          @click="isDailyKmsVisible = !isDailyKmsVisible"
          icon="mdi mdi-chevron-down"
          size="50px"
          class="px-10"
        />
        <v-icon
          v-else
          @click="isDailyKmsVisible = !isDailyKmsVisible"
          icon="mdi mdi-chevron-right"
          size="50px"
          class="px-10"
        />
      </v-row>
      <v-row v-if="isDailyKmsVisible" class="mt-n4 mb-2">
        <v-col>
          <MileageGraph :dataPoints="mileageStore.mileageByEvent" />
        </v-col>
      </v-row>
    </v-container>
    <v-divider />

    <!-- Leaderboard -->
    <v-container class="pa-0">
      <v-row
        align="start"
        @click="isLeaderboardVisible = !isLeaderboardVisible"
        id="pointer-cursor"
        class="my-2"
      >
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
            <tr v-for="entry in eventLeaderboard.leaderboard?.leaderboard" :key="entry.rank">
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
            </tr>
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
import { useMileageStore } from '@/stores/mileage'
import { onMounted, ref } from 'vue'
import type { Event } from '@/types/event'
import router from '@/router'
import { useDisplay } from 'vuetify'
import MileageModal from '../MileageModal.vue'
import MileageGraph from '../MileageGraph.vue'
import type { UserLeaderboard } from '@/types/mileage'
const { mobile } = useDisplay()

const eventStore = useEventStore()
const userStore = useUserStore()
const isDescVisible = ref(true)
const isDailyKmsVisible = ref(false)
const isLeaderboardVisible = ref(false)
const isUserSignedUp = ref(false)
const method = ref()
const mileageStore = useMileageStore()
const dialog = ref(false)

const eventLeaderboard = ref({
  leaderboard: {} as UserLeaderboard | undefined
})

const event = ref<Event>()
onMounted(async () => {
  if (eventStore.events.length < 1) {
    await eventStore.getEvents()
  }
  event.value = eventStore.events.find(
    (e) => e.eventId === Number(router.currentRoute.value.params.id)
  )
  try {
    await mileageStore.getMileageByEvent(event.value?.eventId as number)
    eventLeaderboard.value.leaderboard = (await mileageStore.getLeaderboard({
      type: 'event',
      eventId: event.value?.eventId
    })) as UserLeaderboard
  } catch (error) {
    console.log(error)
  }
  checkUserEvent()
  getIconName(userStore.user?.travelMethod)
})

const signUpEvent = async () => {
  try {
    await userStore.addEvent(event.value?.eventId as number)
  } catch (error) {
    console.log(error)
  }
  isUserSignedUp.value = true
}

const checkUserEvent = () => {
  if (userStore.user?.usersEvents) {
    if (userStore.user?.usersEvents.includes(event.value?.eventId as number))
      isUserSignedUp.value = true
  }
}

const getIconName = (medium: any) => {
  switch (medium) {
    case 'RUNNING':
      method.value = 'mdi-run-fast'
      break
    case 'WHEELING':
      method.value = 'mdi-wheelchair-accessibility'
      break
    case 'WALKING':
      method.value = 'mdi-walk'
      break
  }
}

const getTrophyColour = (rank: number) => {
  switch (rank) {
    case 1:
      return 'text-yellow-darken-1'
    case 2:
      return 'text-blue-grey-lighten-1'
    default:
      return 'text-orange-darken-1'
  }
}

const updateEvent = async () => {
  await eventStore.getEvent(event.value?.eventId as number)
  event.value = eventStore.events.find(
    (e) => e.eventId === Number(router.currentRoute.value.params.id)
  )
}
</script>
<style scoped>
#placeColumn {
  width: 80px;
}

#nameColumn {
  width: auto;
}

#distanceColumn {
  width: 33%;
}
</style>
