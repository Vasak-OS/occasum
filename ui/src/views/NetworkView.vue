<script lang="ts" setup>
import { onMounted, ref, inject, computed } from 'vue';

const $vsk: any = inject('vsk');
const networkInfo = ref({
  interface: 'enp4s0',
  type: 'ethernet',
  name: 'Conexi\u00f3n cableada 1',
  connected: true,
  icon: '/usr/share/icons/Fluent-teal-dark/symbolic/status/network-wired-symbolic.svg',
  ip: '192.168.0.1'
});

async function setNetwork() {
  networkInfo.value = JSON.parse(await $vsk.getNetworkInfo());
  console.log('networkInfo', networkInfo.value);
}

const status = computed(() => {
  return networkInfo.value.connected ? 'connected' : 'disconnected';
});

onMounted(() => {
  setNetwork();
});
</script>

<template>
  <div class="ocassum-network">
    <div class="ocassum-network-status-card">
      <div class="ocassum-network-status-card-icon">
        <img :src="networkInfo.icon" alt="Network icon" />
      </div>

      <h2>
        {{ networkInfo.interface }}
        <span class="network-status" :class="status">&nbsp;</span>
      </h2>
      <p>{{ networkInfo.name }}</p>
      <div>
        <p>{{ networkInfo.ip }}</p>
      </div>
    </div>
  </div>
</template>
