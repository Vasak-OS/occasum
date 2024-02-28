<script lang="ts" setup>
import { SideBar, SideButton, WindowFrame } from '@vasakgroup/vue-libvasak';
import routers from '@/routers/index';
import { computed, inject, ref } from 'vue';

var section = ref('INFO');
const $vsk: any = inject('vsk');
const routersData = ref(routers);
const image = ref('');

const changeSection = (newSection: string) => {
  console.log('changeSection', newSection);
  section.value = newSection;
};

const routerComponent = computed(() => {
  return routers.find((r: any) => r.tag === section.value)?.component;
});

const getImage = (image: string): Promise<string> => {
  return $vsk.getIcon(image);
};

const appImage = computed(() => {
  return image.value;
});

routersData.value.forEach((router: any) => {
  getImage(router.image).then((img: string) => {
    router.image = img;
  });
});

getImage('configurator').then((img: string) => {
  image.value = img;
});
</script>

<template>
  <WindowFrame title="Occasum" :image="appImage">
    <div class="flex">
      <SideBar>
        <SideButton
          v-for="router in routersData"
          :key="router.tag"
          :title="router.title"
          :image="router.image"
          @click="changeSection(router.tag)"
        />
      </SideBar>

      <div class="p-3 col side-content-area">
        <transition name="slide-fade" mode="out-in" appear>
          <component :is="routerComponent"></component>
        </transition>
      </div>
    </div>
  </WindowFrame>
</template>