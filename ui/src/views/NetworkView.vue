<script lang="ts" setup>
import { onMounted, ref, inject } from 'vue';

const $vsk: any = inject('vsk');
const networkInfo = ref({});

async function setNetwork() {
  networkInfo.value = await $vsk.getNetworkInfo();
}

onMounted(() => {
  setNetwork();
});
</script>

<template>
  <div>
    <h1>Network</h1>
    <p>{{ networkInfo }}</p>
  </div>
</template>
