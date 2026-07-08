<script setup>
import ImagePicker from '@/components/ImagePicker.vue'

const props = defineProps({
  fields: { type: Array, required: true },
  modelValue: { type: Object, required: true },
})
const emit = defineEmits(['update:modelValue'])

function set(key, value) {
  emit('update:modelValue', { ...props.modelValue, [key]: value })
}

function tagsToText(arr) {
  return Array.isArray(arr) ? arr.join(', ') : ''
}
function textToTags(text) {
  return text.split(',').map((s) => s.trim()).filter(Boolean)
}

const socialKeys = [
  { key: 'linkedin', label: 'LinkedIn' },
  { key: 'twitter', label: 'Twitter / X' },
  { key: 'github', label: 'GitHub' },
  { key: 'email', label: 'Email' },
]
function setSocial(key, socialsObj, sKey, value) {
  set(key, { ...(socialsObj || {}), [sKey]: value })
}
</script>

<template>
  <div class="space-y-5">
    <div v-for="f in fields" :key="f.key">
      <label class="label">{{ f.label }}<span v-if="f.required" class="text-red-500 ml-0.5">*</span></label>

      <input v-if="f.type === 'text'"
             :value="modelValue[f.key]" @input="set(f.key, $event.target.value)"
             type="text" class="input" :placeholder="f.placeholder" />

      <input v-else-if="f.type === 'number'"
             :value="modelValue[f.key]" @input="set(f.key, Number($event.target.value))"
             type="number" class="input" :placeholder="f.placeholder" />

      <textarea v-else-if="f.type === 'textarea'"
                :value="modelValue[f.key]" @input="set(f.key, $event.target.value)"
                class="input" :rows="f.rows || 3" :placeholder="f.placeholder"></textarea>

      <select v-else-if="f.type === 'select'"
              :value="modelValue[f.key]" @change="set(f.key, $event.target.value)"
              class="input">
        <option v-for="opt in f.options" :key="opt" :value="opt">{{ opt }}</option>
      </select>

      <label v-else-if="f.type === 'boolean'" class="flex items-center gap-2 cursor-pointer">
        <input type="checkbox" :checked="modelValue[f.key]" @change="set(f.key, $event.target.checked)"
               class="w-4 h-4 rounded accent-emerald-brand-500" />
        <span class="text-sm text-navy-600">{{ modelValue[f.key] ? 'Aktif / tayang' : 'Nonaktif / draft' }}</span>
      </label>

      <ImagePicker v-else-if="f.type === 'image'"
                   :model-value="modelValue[f.key]" @update:model-value="set(f.key, $event)" />

      <input v-else-if="f.type === 'tags'"
             :value="tagsToText(modelValue[f.key])"
             @input="set(f.key, textToTags($event.target.value))"
             type="text" class="input" :placeholder="f.placeholder || 'Pisahkan dengan koma'" />

      <div v-else-if="f.type === 'socials'" class="grid grid-cols-2 gap-3">
        <input v-for="sk in socialKeys" :key="sk.key"
               :value="(modelValue[f.key] || {})[sk.key] || ''"
               @input="setSocial(f.key, modelValue[f.key], sk.key, $event.target.value)"
               type="text" class="input !text-xs" :placeholder="sk.label" />
      </div>
    </div>
  </div>
</template>
