import InfoView from '@/views/InfoView.vue';
import NetworkViewVue from '@/views/NetworkView.vue';
import StyleView from '@/views/StyleView.vue';

const routers: Array<any> = [
  {
    title: 'Info',
    image: 'help-info',
    tag: 'INFO',
    component: InfoView
  },
  {
    title: 'Style',
    image: 'style',
    tag: 'STYLE',
    component: StyleView
  },
  {
    title: 'Network',
    image: 'networkmanager',
    tag: 'NETWORK',
    component: NetworkViewVue
  }
];

export default routers;
