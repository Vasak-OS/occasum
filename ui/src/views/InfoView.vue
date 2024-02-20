<script lang="ts" setup>
import { onMounted, ref, inject } from 'vue';

const sysInfo = ref({
  os: 'platform.system()',
  release: 'platform.release()',
  version: 'platform.version()',
  machine: 'platform.machine()',
  processor: 'platform.processor()',
  architecture: 'platform.architecture()',
  system: 'platform.system()',
  uname: 'platform.uname()',
  ram: 'os.sysconf()',
  cpu_count: 'os.cpu_count()',
  hostname: 'platform.node()',
  username: 'os.getlogin()'
});

const $vsk: any = inject('vsk');

async function setInfo() {
  const newInfo = await $vsk.getOSInfo();
  console.log('newInfo', newInfo);

  sysInfo.value = JSON.parse(newInfo);
}

onMounted(() => {
  setInfo();
});
</script>

<template>
  <div>
    <h1>Info</h1>

    <div class="info-table">
      <table class="table">
        <tbody>
          <tr v-for="(value, key) in sysInfo" :key="key">
            <th scope="row">{{ key }}</th>
            <td>{{ value }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
.info-table {
  padding: 20px 50px;
}

.table {
  background-color: var(--system-background);
  border-radius: var(--system-border);
}

.table th,
.table td {
  background-color: transparent;
  color: var(--system-text);
  border-color: var(--system-background);
}
</style>
