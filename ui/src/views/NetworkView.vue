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
  return networkInfo.value.connected ? 'text-success' : 'text-danger';
});

onMounted(() => {
  setNetwork();
});
</script>

<template>
  <div>
    <div class="card">
      <div class="row g-0">
        <div class="col-md-3">
          <img :src="networkInfo.icon" class="img-fluid w-100" alt="Network icon" />
        </div>
        <div class="col-md-9">
          <div class="card-body">
            <h5 class="card-title">{{ networkInfo.interface }} <span class="network-status" :class="status">●</span></h5>
              <p class="card-text">{{ networkInfo.name }} <br/> {{ networkInfo.ip }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<style>
.card {
  background-color: var(--system-background);
  border-radius: var(--system-border);
  color: var(--system-text);
  margin: 10px;
  padding: 10px;
}
</style>