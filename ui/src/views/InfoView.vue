<script lang="ts" setup>
import { onMounted, ref, inject } from 'vue';

const $vsk: any = inject('vsk');
const section = 'INFO';
const logo = ref('');

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

async function setInfo() {
  const newInfo = await $vsk.getOSInfo();
  sysInfo.value = JSON.parse(newInfo);
}

const getConfig = (configName: string) => {
  return $vsk.getConfig(section, configName);
};

onMounted(async () => {
  setInfo();
  logo.value = await getConfig('logo');
});
</script>

<template>
  <div>
    <img :src="logo" class="ocassum-info-logo" alt="Logo" />
    <table>
      <tbody>
        <tr v-for="(value, key) in sysInfo" :key="key">
          <th scope="row">{{ key }}</th>
          <td>{{ value }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
