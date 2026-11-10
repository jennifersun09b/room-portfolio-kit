/* RoomKit Studio - the page side. Plain JavaScript, no build step, works offline. */
(() => {
  'use strict';

  // ------------------------------------------------------------------ basics
  const TOKEN = document.querySelector('meta[name="roomkit-token"]').content;
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));
  const esc = (v) => String(v == null ? '' : v).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const enc = encodeURIComponent;
  const clone = (o) => JSON.parse(JSON.stringify(o));
  const MODEL_EXT = ['glb', 'gltf', 'obj', 'fbx', 'stl'];

  const STEPS = [
    { id: 'persona', title: 'Who are you?', icon: 'user' },
    { id: 'profile', title: 'Your details', icon: 'idcard' },
    { id: 'projects', title: 'Your projects', icon: 'image' },
    { id: 'room', title: 'Choose a room', icon: 'cube' },
    { id: 'furnish', title: 'Make it yours', icon: 'sofa' },
    { id: 'build', title: 'Build & publish', icon: 'sparkles' },
  ];

  const S = {
    status: null, rooms: [], roomsScanning: false, personas: [], linkTypes: {}, exportsInfo: {},
    projects: [], pid: null, profile: null, studio: null, outputs: {}, folder: '',
    step: 'persona', job: null, jobSince: 0, saveTimer: null, saving: false, savedAt: 0, roomFilter: 'for-you',
    openSlot: null, showLog: false, logLines: [],
  };

  // ------------------------------------------------------------------ icons (24px stroke icons)
  const P = (d) => `<path d="${d}"/>`;
  const ICONS = {
    check: P('M5 12.5l4.5 4.5L19 7.5'), chev: P('M6 9l6 6 6-6'), x: P('M6 6l12 12M18 6 6 18'), plus: P('M12 5v14M5 12h14'),
    right: P('M5 12h14M13 6l6 6-6 6'), left: P('M19 12H5M11 6l-6 6 6 6'), up: P('M12 19V5M6 11l6-6 6 6'), down: P('M12 5v14M6 13l6 6 6-6'),
    grip: '<path stroke-width="3.2" d="M9 6h.01M15 6h.01M9 12h.01M15 12h.01M9 18h.01M15 18h.01"/>',
    trash: P('M4 7h16M9 7V4.5h6V7M6.5 7l1 13h9l1-13M10 11v6M14 11v6'),
    sliders: P('M4 7h9M17 7h3M4 17h3M11 17h9') + '<circle cx="15" cy="7" r="2"/><circle cx="9" cy="17" r="2"/>',
    folder: P('M3 7.5A1.5 1.5 0 0 1 4.5 6H9l2 2h8.5A1.5 1.5 0 0 1 21 9.5v8a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 17.5z'),
    download: P('M12 4v11M7 10l5 5 5-5M5 20h14'), upload: P('M12 16V5M7 10l5-5 5 5M5 20h14'),
    globe: '<circle cx="12" cy="12" r="9"/>' + P('M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z'),
    cube: P('M12 3l8 4.5v9L12 21l-8-4.5v-9zM12 12l8-4.5M12 12 4 7.5M12 12v9'),
    image: '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="8.5" cy="9.5" r="1.5"/>' + P('M3 17l5-5 4 4 3-3 6 6'),
    link: P('M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1'),
    sparkles: P('M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8zM19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z'),
    dice: '<rect x="4" y="4" width="16" height="16" rx="3.5"/><path stroke-width="3" d="M9 9h.01M15 15h.01M15 9h.01M9 15h.01M12 12h.01"/>',
    copy: '<rect x="9" y="9" width="11" height="11" rx="2"/>' + P('M5 15V6a1 1 0 0 1 1-1h9'),
    external: P('M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5'),
    clock: '<circle cx="12" cy="12" r="9"/>' + P('M12 7v5l3 2'),
    alert: P('M12 3.5 21.5 20h-19zM12 10v4.5') + '<path stroke-width="2.6" d="M12 17.3h.01"/>',
    info: '<circle cx="12" cy="12" r="9"/>' + P('M12 11v5') + '<path stroke-width="2.6" d="M12 7.6h.01"/>',
    play: P('M7 5l12 7-12 7z'), stop: '<rect x="6" y="6" width="12" height="12" rx="2"/>',
    refresh: P('M20 11a8 8 0 1 0-2.3 5.7M20 5v6h-6'), key: '<circle cx="8" cy="15" r="4"/>' + P('M11 12l9-9M16 7l3 3M14 9l2 2'),
    user: '<circle cx="12" cy="8" r="4"/>' + P('M4 21c1-4.5 4.3-7 8-7s7 2.5 8 7'),
    idcard: '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="11" r="2.2"/>' + P('M5.8 16.5c.6-1.6 1.8-2.4 3.2-2.4s2.6.8 3.2 2.4M14.5 10h4M14.5 13.5h3'),
    pen: P('M4 20l4-1 11-11-3-3L5 16zM14 6l3 3'), brush: P('M18.5 3.5l2 2-8.5 9.5-3-3zM9 12c-2.2 0-4 1.6-4 3.8 0 1.4-.6 2.6-2 3.7 3.6.8 8.2-.2 8.9-4.5'),
    store: P('M3.5 9 5 4h14l1.5 5M4.5 9v11h15V9M3 9h18M9.5 20v-5.5h5V20'),
    video: '<rect x="3" y="6" width="13" height="12" rx="2"/>' + P('M16 10.5l5-3v9l-5-3'),
    cap: P('M2 9.5 12 5l10 4.5L12 14zM6 11.5v4.5c2.5 2.3 9.5 2.3 12 0v-4.5M21.5 9.5v5'),
    book: P('M5 4.5A1.5 1.5 0 0 1 6.5 3H19v15H6.5A1.5 1.5 0 0 0 5 19.5zM5 19.5A1.5 1.5 0 0 0 6.5 21H19v-3'),
    board: '<rect x="3" y="4" width="18" height="12" rx="1.5"/>' + P('M8 20l4-4 4 4M7 8.5h6M7 11.5h9'),
    heart: P('M12 20s-7.5-4.6-9-9.5C2 6.9 4.4 4.5 7.2 4.5c1.9 0 3.4 1 4.8 2.7 1.4-1.7 2.9-2.7 4.8-2.7 2.8 0 5.2 2.4 4.2 6C19.5 15.4 12 20 12 20z'),
    // furniture
    bed: P('M3 19V6M3 14h18v5M21 19v-2M3 14v-2.5A1.5 1.5 0 0 1 4.5 10H9v4M9 14v-3h8.5a3.5 3.5 0 0 1 3.5 3.5'),
    sofa: P('M5 11V8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v3M3 12.5a2 2 0 0 1 4 0V15h10v-2.5a2 2 0 0 1 4 0V18H3zM5 18v2M19 18v2'),
    chair: P('M7.5 3h9v8.5h-9zM6 11.5h12V15H6zM7.5 15v6M16.5 15v6'),
    stool: P('M6 5.5h12V9H6zM8.5 9 6.5 21M15.5 9l2 12M7.6 15h8.8'),
    table: P('M3 8h18v3H3zM5 11v9M19 11v9'), desk: P('M3 8h18M4 8v12M20 8v12M14 8v6h6M14 11h6'),
    lamp: P('M8 3h8l3 8H5zM12 11v7M8 21h8'), floor_lamp: P('M9 3h6l2 5H7zM12 8v13M8 21h8'),
    pendant_lamp: P('M12 2v6M6 14a6 6 0 0 1 12 0zM10.2 17.5a2 2 0 0 0 3.6 0'),
    plant: P('M12 21v-8M12 13c0-4 3-7 7-7 0 4-3 7-7 7zM12 15.5c0-3-2.5-5.5-6-5.5 0 3 2.5 5.5 6 5.5zM7.5 21h9'),
    hanging_plant: P('M12 2v5M7 7h10l-1.5 5h-7zM9 12c-.8 3-2.5 4.5-4 7M15 12c.8 3 2.5 4.5 4 7M12 12v6'),
    rug: '<rect x="4" y="6" width="16" height="12" rx="1"/>' + P('M2 9h2M2 12h2M2 15h2M20 9h2M20 12h2M20 15h2M8.5 9.5h7v5h-7z'),
    frame: '<rect x="4" y="3" width="16" height="18" rx="1"/><rect x="7" y="6" width="10" height="10"/>' + P('M7 14l3-3 3 3 1.5-1.5L17 15'),
    shelf: '<rect x="4" y="3" width="16" height="18" rx="1"/>' + P('M4 9h16M4 15h16M8 3v6M15 9v6M10 15v6'),
    cabinet: '<rect x="4" y="4" width="16" height="16" rx="1.5"/>' + P('M4 12h16M10 8h4M10 16h4'),
    monitor: '<rect x="3" y="4" width="18" height="12" rx="1.5"/>' + P('M9 20h6M12 16v4'),
    pet: '<circle cx="6.5" cy="10" r="1.8"/><circle cx="10" cy="6" r="1.8"/><circle cx="14" cy="6" r="1.8"/><circle cx="17.5" cy="10" r="1.8"/>' + P('M12 20.5c-3 0-5-1.6-5-3.6s2.2-4.4 5-4.4 5 2.4 5 4.4-2 3.6-5 3.6z'),
    instrument: P('M9 18V5l11-2v13') + '<circle cx="6" cy="18" r="3"/><circle cx="17" cy="16" r="3"/>',
    speaker: '<rect x="6" y="3" width="12" height="18" rx="2"/><circle cx="12" cy="14" r="3"/><circle cx="12" cy="7.5" r="1"/>',
    counter: P('M2 9h20v3H2zM3 12v8h18v-8M9 12v8M15 12v8'), easel: P('M12 3v2M6 5h12v10H6zM8.5 15l-2.5 6M15.5 15l2.5 6M12 15v4'),
    star: P('M12 3l2.8 5.7 6.2.9-4.5 4.4 1 6.2L12 17.3l-5.5 2.9 1-6.2L3 9.6l6.2-.9z'),
    mirror: '<ellipse cx="12" cy="10" rx="6" ry="7.5"/>' + P('M12 17.5V21M8 21h8M9.5 7.5l2-2'),
    telescope: P('M3 13.5 15 7.5l2 4-12 6zM15 7.5l3-1.5 2 4-3 1.5M10.5 15.2 8 21M10.5 15.2 13 21'),
    trunk: '<rect x="3" y="7" width="18" height="13" rx="1.5"/>' + P('M3 12h18M9 7V4.5h6V7M11 12v3h2v-3'),
    fireplace: P('M3 4h18v3H3zM5 7v13M19 7v13M3 20h18M9 20v-4.5a3 3 0 0 1 6 0V20'),
    rack: P('M4 5h16M6 5v15M18 5v15M4 20h4M16 20h4M10 5v2.5L8 15h4l-2-7.5M14.5 5v2.5l-2 7.5h4l-2-7.5'),
    vanity: P('M4 12h16v2H4zM6 14v6M18 14v6') + '<ellipse cx="12" cy="7" rx="4" ry="4.5"/>',
  };
  const SLOT_ICON = {
    desk: 'desk', chair: 'chair', stool: 'stool', sofa: 'sofa', armchair: 'sofa', bed: 'bed', bunk_bed: 'bed', table: 'table',
    side_table: 'cabinet', counter: 'counter', display_case: 'cabinet', shelf: 'shelf', wall_shelf: 'shelf', bookcase: 'shelf',
    cabinet: 'cabinet', media_console: 'cabinet', workbench: 'table', easel: 'easel', monitor: 'monitor', instrument: 'instrument',
    speaker: 'speaker', hero_prop: 'star', lamp: 'lamp', floor_lamp: 'floor_lamp', pendant_lamp: 'pendant_lamp', plant: 'plant',
    hanging_plant: 'hanging_plant', planter: 'plant', rug: 'rug', wall_art: 'frame', pet: 'pet', clothes_rack: 'rack', wardrobe: 'cabinet',
    vanity: 'vanity', mirror: 'mirror', telescope: 'telescope', trunk: 'trunk', fireplace: 'fireplace', stove: 'fireplace',
    salon_chair: 'chair', window_seat: 'sofa',
  };
  const icon = (name, cls = '') => `<svg class="ic ${cls}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">${ICONS[name] || ICONS.cube}</svg>`;

  // ------------------------------------------------------------------ server calls
  async function api(path, opts = {}) {
    const headers = { 'X-RoomKit-Token': TOKEN };
    let body = opts.body;
    if (body && !(body instanceof Blob)) { headers['Content-Type'] = 'application/json'; body = JSON.stringify(body); }
    let res;
    try {
      res = await fetch('/api/' + path, { method: opts.method || 'GET', headers, body });
    } catch (e) {
      throw new Error('Studio has stopped. Start it again with Start.command / Start.bat, then reload this page.');
    }
    const data = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(data.error || 'Something went wrong. Try again.');
    return data;
  }

  function toast(msg, kind = 'info', ms = 4200) {
    const el = document.createElement('div');
    el.className = `toast ${kind}`;
    el.innerHTML = `${icon(kind === 'error' ? 'alert' : kind === 'ok' ? 'check' : 'info')}<span>${esc(msg)}</span>`;
    $('#toasts').appendChild(el);
    setTimeout(() => { el.classList.add('out'); setTimeout(() => el.remove(), 300); }, ms);
  }

  // ------------------------------------------------------------------ helpers about data
  const persona = () => S.personas.find((p) => p.id === S.studio?.persona) || null;
  const room = (id = S.studio?.room) => S.rooms.find((r) => r.id === id) || null;
  const theme = (r = room()) => r ? (r.themes.find((t) => t.id === S.studio.theme) || r.themes.find((t) => t.default) || r.themes[0]) : null;
  const projectUrl = (rel) => `/p/${enc(S.pid)}/${rel.split('/').map(enc).join('/')}`;
  const themeImage = (t) => t && (t.thumb || t.preview) ? `/kit/${(t.thumb || t.preview)}` : '';
  const fmtDur = (s) => {
    s = Math.max(0, Math.round(s));
    if (s < 10) return `${Math.max(1, s)} s`;
    if (s < 50) return `${Math.round(s / 5) * 5} s`;
    const m = Math.round(s / 60);
    return m < 60 ? `${m} min` : `${Math.floor(m / 60)} h ${m % 60} min`;
  };
  const ago = (t) => {
    const s = Date.now() / 1000 - t;
    if (s < 60) return 'just now';
    if (s < 3600) return `${Math.round(s / 60)} min ago`;
    if (s < 86400) return `${Math.round(s / 3600)} h ago`;
    return new Date(t * 1000).toLocaleDateString();
  };
  const signLimits = (kind = 'name') => {
    const r = room();
    const sign = r && r[kind + '_sign'];
    return sign || (kind === 'name' ? { fit: 14, max: 22 } : { fit: 24, max: 40 });
  };

  function linkRows() {
    const links = S.profile.links || {};
    const order = (S.studio.link_order || []).slice();
    Object.keys(links).forEach((k) => { if (!order.includes(k)) order.push(k); });
    return order.map((type) => ({ type, value: links[type] || '' }));
  }
  function setLinkRows(rows) {
    S.studio.link_order = rows.map((r) => r.type);
    S.profile.links = {};
    rows.forEach((r) => { if (r.value.trim()) S.profile.links[r.type] = r.value.trim(); });
  }

  function validateLink(type, value) {
    const v = (value || '').trim();
    if (!v) return { level: '', msg: '' };
    if (type === 'email') {
      return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.replace(/^mailto:/, '')) ? { level: 'ok', msg: '' }
        : { level: 'error', msg: 'This doesn’t look like an email address (like you@example.com).' };
    }
    if (/^https?:\/\/[^\s.]+\.[^\s]{2,}/i.test(v)) return { level: 'ok', msg: '' };
    return { level: 'error', msg: 'Start with https:// — for example https://' + (type === 'website' ? 'yourname.com' : 'example.com/you') };
  }
  function tidyLink(type, value) {
    let v = (value || '').trim();
    if (!v || type === 'email') return v.replace(/^mailto:/i, '');
    const info = S.linkTypes[type] || {};
    if (v.startsWith('@') && info.prefix) return info.prefix + v.slice(1);
    if (!/^https?:\/\//i.test(v)) {
      if (/^[\w-]+$/.test(v) && info.prefix) return info.prefix + v;
      if (/^[^\s]+\.[^\s]{2,}/.test(v)) return 'https://' + v;
    }
    return v;
  }

  function nameCheck() {
    const n = (S.profile.name || '').trim();
    const lim = signLimits('name');
    const r = room();
    const where = r ? `the sign in the ${r.name}` : 'the room’s sign';
    if (!n) return { level: 'error', msg: 'Add your name (or your shop’s name). It goes on ' + where + '.' };
    if (n.length > lim.max) return { level: 'error', msg: `Your name is too long for ${where}. Try ${lim.max} characters or fewer.` };
    if (n.length > lim.fit) return { level: 'warn', msg: `Fits, but it will be made a little smaller. ${lim.fit} characters or fewer looks best on ${where}.` };
    return { level: 'ok', msg: `Fits nicely on ${where}.` };
  }
  function roleCheck() {
    const n = (S.profile.role || '').trim();
    const lim = signLimits('role');
    if (!n) return { level: 'warn', msg: 'Add a short line under your name, like your job or what you sell.' };
    if (n.length > lim.max) return { level: 'error', msg: `That’s long for the sign. Try ${lim.max} characters or fewer.` };
    if (n.length > lim.fit) return { level: 'warn', msg: `It will be made a little smaller to fit. ${lim.fit} characters or fewer looks best.` };
    return { level: 'ok', msg: '' };
  }

  function stepState(id) {
    const p = S.profile, st = S.studio;
    switch (id) {
      case 'persona': return st.persona ? { done: true, sub: persona()?.label || '' } : { done: false, sub: 'Pick what fits you' };
      case 'profile': return p.name ? { done: nameCheck().level !== 'error', sub: p.name } : { done: false, sub: 'Name, links, colours' };
      case 'projects': {
        const n = (p.projects || []).filter((x) => x.image).length;
        return { done: n > 0, sub: n ? `${n} with pictures` : 'Pictures of your work' };
      }
      case 'room': { const r = room(); return r ? { done: true, sub: `${r.name} · ${theme(r)?.label || ''}` } : { done: false, sub: 'Pick your room' }; }
      case 'furnish': { const n = (st.swaps || []).length; return { done: n > 0, optional: true, sub: n ? `${n} of your own` : 'Optional' }; }
      case 'build': return st.last_build ? { done: true, sub: `Built ${ago(st.last_build.when)}` } : { done: false, sub: 'Pictures + website' };
      default: return { done: false, sub: '' };
    }
  }

  // ------------------------------------------------------------------ saving
  function changed(opts = {}) {
    clearTimeout(S.saveTimer);
    setSaveState('pending');
    S.saveTimer = setTimeout(save, opts.now ? 0 : 650);
    renderSide();
  }
  async function save() {
    if (!S.pid) return;
    S.saving = true;
    setSaveState('saving');
    try {
      S.profile.room = S.studio.room || '';
      S.profile.theme = S.studio.theme || '';
      if (!S.studio.brand_on) S.profile.brand_color = '';
      await api(`projects/${enc(S.pid)}`, { method: 'PUT', body: { profile: S.profile, studio: S.studio } });
      S.savedAt = Date.now();
      setSaveState('saved');
    } catch (e) {
      setSaveState('error');
      toast(e.message, 'error');
    } finally { S.saving = false; }
  }
  function setSaveState(state) {
    const el = $('#save-state');
    if (!el) return;
    const words = { pending: 'Unsaved changes', saving: 'Saving…', saved: 'All changes saved', error: 'Not saved' };
    el.dataset.state = state;
    el.innerHTML = `${icon(state === 'error' ? 'alert' : state === 'saved' ? 'check' : 'clock')}<span>${words[state]}</span>`;
  }

  // ------------------------------------------------------------------ boot
  async function boot() {
    try {
      const [status, rooms, personas, projects] = await Promise.all([api('status'), api('rooms'), api('personas'), api('projects')]);
      S.status = status;
      S.rooms = rooms.rooms || [];
      S.roomsScanning = rooms.scanning;
      S.personas = personas.personas || [];
      S.linkTypes = personas.link_types || {};
      S.exportsInfo = personas.exports || {};
      S.projects = projects;
    } catch (e) {
      $('#app').innerHTML = `<div class="fatal">${icon('alert')}<h1>Studio isn’t running</h1><p>${esc(e.message)}</p></div>`;
      return;
    }
    const hash = new URLSearchParams(location.hash.slice(1));
    const last = hash.get('p') || safeStorage('get', 'roomkit.project');
    const pick = S.projects.find((p) => p.id === last) || null;
    if (pick) await openProject(pick.id, hash.get('s'));
    else renderWelcome();
    pollStatus();
    if (S.roomsScanning || S.status.blender.state === 'checking') pollRooms();
  }

  function safeStorage(op, key, value) {
    try {
      if (op === 'get') return localStorage.getItem(key);
      if (op === 'set') localStorage.setItem(key, value);
      if (op === 'del') localStorage.removeItem(key);
    } catch (e) { /* private mode: fine */ }
    return null;
  }

  async function pollStatus() {
    try {
      const st = await api('status');
      const was = S.status && S.status.blender.state;
      S.status = st;
      if (was !== st.blender.state) { renderTop(); if (S.step === 'build' && !S.job) renderMain(); }
      if (st.job && st.job.state === 'running' && st.job.project === S.pid && !S.job) { S.job = st.job; S.jobSince = 0; S.step = 'build'; render(); pollJob(); }
    } catch (e) { /* ignore - shown when the user acts */ }
    setTimeout(pollStatus, S.status && S.status.blender.state === 'checking' ? 1500 : 8000);
  }
  async function pollRooms() {
    try {
      const r = await api('rooms');
      const before = JSON.stringify(S.rooms.map((x) => [x.id, x.source, x.thumb]));
      S.rooms = r.rooms || [];
      S.roomsScanning = r.scanning;
      if (before !== JSON.stringify(S.rooms.map((x) => [x.id, x.source, x.thumb])) && S.pid) {
        if (['room', 'furnish', 'persona'].includes(S.step)) renderMain();
        renderSide();
      }
      if (r.scanning) setTimeout(pollRooms, 2500);
    } catch (e) { setTimeout(pollRooms, 5000); }
  }

  async function openProject(pid, step) {
    const data = await api(`projects/${enc(pid)}`);
    S.pid = data.id; S.folder = data.folder;
    S.profile = Object.assign({ name: '', role: '', tagline: '', brand_color: '', links: {}, skills: [], projects: [] }, data.profile);
    S.studio = Object.assign({ persona: '', room: '', theme: '', seed: 1, swaps: [], build: { quality: 'quick', web: true, exports: ['hero'] }, touched: {}, link_order: [] }, data.studio);
    S.studio.touched = S.studio.touched || {};
    S.studio.build = Object.assign({ quality: 'quick', web: true, exports: ['hero'] }, S.studio.build || {});
    if (S.studio.brand_on === undefined) S.studio.brand_on = !!S.profile.brand_color;
    if (!S.studio.room && S.profile.room) S.studio.room = S.profile.room;
    if (!S.studio.theme && S.profile.theme) S.studio.theme = S.profile.theme;
    S.outputs = data.outputs || {};
    const want = step || S.studio.step;
    S.step = STEPS.some((s) => s.id === want) ? want : 'persona';
    S.job = null;
    safeStorage('set', 'roomkit.project', pid);
    setHash();
    render();
  }

  // ------------------------------------------------------------------ welcome (no project open)
  function renderWelcome() {
    S.pid = null;
    const list = S.projects.map((p) => `
      <button class="proj-tile" data-open="${esc(p.id)}">
        <span class="proj-thumb">${p.hero ? `<img src="${esc(p.hero)}" alt="">` : icon('cube')}</span>
        <span class="proj-meta"><strong>${esc(p.name)}</strong><small>${esc(p.person || 'No name yet')} · ${esc(ago(p.updated))}</small></span>
        ${icon('right', 'chev')}
      </button>`).join('');
    const hero = S.rooms.filter((r) => r.thumb).slice(0, 6).map((r) => `<img src="/kit/${esc(r.thumb)}" alt="">`).join('');
    $('#app').innerHTML = `
      <div class="welcome">
        <div class="welcome-card">
          <div class="brand big">${logo()}<span>RoomKit <b>Studio</b></span></div>
          <h1>Your work, in a cosy 3D room.</h1>
          <p class="lead">Fill in a few friendly forms, pick a room, and RoomKit makes your portfolio pictures and a clickable website. No Blender skills needed.</p>
          <form class="new-proj" id="new-proj">
            <label for="np-name">Name your project</label>
            <div class="row">
              <input id="np-name" required maxlength="60" placeholder="e.g. My portfolio" value="${S.projects.length ? '' : 'My portfolio'}">
              <button class="btn primary" type="submit">${icon('plus')}Create project</button>
            </div>
            <button class="link-btn" type="button" id="np-example">${icon('sparkles')}Or start with an example you can edit</button>
          </form>
          ${list ? `<div class="proj-list"><h2>Continue a project</h2>${list}</div>` : ''}
        </div>
        <div class="welcome-art" aria-hidden="true">${hero}</div>
      </div>`;
    $('#new-proj').addEventListener('submit', async (e) => {
      e.preventDefault();
      try { const d = await api('projects', { method: 'POST', body: { name: $('#np-name').value } }); S.projects = await api('projects'); await openProject(d.id); }
      catch (err) { toast(err.message, 'error'); }
    });
    $('#np-example').addEventListener('click', async () => {
      try {
        const d = await api('projects', { method: 'POST', body: { name: 'Example portfolio' } });
        await api(`projects/${enc(d.id)}/sample`, { method: 'POST' });
        S.projects = await api('projects');
        await openProject(d.id);
        S.studio.persona = 'student';
        S.studio.room = S.studio.room || 'cozy_bedroom';
        changed();
        render();
        toast('Example loaded. Change anything you like.', 'ok');
      } catch (err) { toast(err.message, 'error'); }
    });
    $$('[data-open]').forEach((b) => b.addEventListener('click', () => openProject(b.dataset.open).catch((e) => toast(e.message, 'error'))));
  }

  const logo = () => `<svg class="logo" viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="16" fill="var(--primary)"/><path d="M32 13 51 24v21L32 55 13 45V24z" fill="#8F84FF"/><path d="M32 13 51 24 32 35 13 24z" fill="#FFF3E4"/><path d="M13 24l19 11v20L13 45z" fill="#FFD9B8"/><path d="M32 35l19-11v21L32 55z" fill="#C9C2FF"/><path d="M19 33l7 4v7l-7-4z" fill="var(--primary)"/></svg>`;

  // ------------------------------------------------------------------ app shell
  function render() {
    if (!S.pid) return renderWelcome();
    $('#app').innerHTML = `
      <header class="topbar" id="topbar"></header>
      <div class="shell">
        <nav class="steps" id="steps" aria-label="Steps"></nav>
        <main id="main" class="main" tabindex="-1"></main>
        <aside class="summary" id="summary" aria-label="Your portfolio"></aside>
      </div>`;
    renderTop(); renderSide(); renderMain();
  }

  function renderTop() {
    const el = $('#topbar');
    if (!el) return;
    const b = S.status.blender;
    const pill = b.state === 'ok' ? `<span class="dot ok"></span>Blender ${esc(b.version)}`
      : b.state === 'checking' ? `<span class="dot wait"></span>Looking for Blender…` : `<span class="dot bad"></span>Blender needed`;
    el.innerHTML = `
      <div class="brand">${logo()}<span>RoomKit <b>Studio</b></span></div>
      <div class="proj-switch">
        <button class="btn ghost" id="proj-btn" aria-haspopup="true" aria-expanded="false">${icon('folder')}<span>${esc(S.pid)}</span>${icon('chev', 'sm')}</button>
        <div class="menu" id="proj-menu" hidden></div>
      </div>
      <div id="save-state" class="save-state" aria-live="polite"></div>
      <div class="top-right">
        <button class="pill ${b.state === 'ok' ? '' : 'warn'}" id="blender-pill">${pill}</button>
        <button class="btn ghost" id="settings-btn">${icon('sliders')}<span>Settings</span></button>
      </div>`;
    setSaveState(S.savedAt ? 'saved' : 'saved');
    $('#settings-btn').onclick = () => openSettings();
    $('#blender-pill').onclick = () => openSettings('blender');
    $('#proj-btn').onclick = (e) => toggleProjectMenu(e.currentTarget);
  }

  async function toggleProjectMenu(btn) {
    const menu = $('#proj-menu');
    if (!menu.hidden) { menu.hidden = true; btn.setAttribute('aria-expanded', 'false'); return; }
    S.projects = await api('projects').catch(() => S.projects);
    menu.innerHTML = S.projects.map((p) => `<button class="menu-item ${p.id === S.pid ? 'current' : ''}" data-p="${esc(p.id)}">
        <span class="mi-thumb">${p.hero ? `<img src="${esc(p.hero)}" alt="">` : icon('cube')}</span><span><strong>${esc(p.name)}</strong><small>${esc(ago(p.updated))}</small></span></button>`).join('')
      + `<hr><button class="menu-item" data-new="1">${icon('plus')}<span><strong>New project</strong></span></button>
         <button class="menu-item" data-folder="1">${icon('folder')}<span><strong>Open project folder</strong></span></button>`;
    menu.hidden = false; btn.setAttribute('aria-expanded', 'true');
    const close = (ev) => { if (!menu.contains(ev.target) && ev.target !== btn) { menu.hidden = true; btn.setAttribute('aria-expanded', 'false'); document.removeEventListener('click', close); } };
    setTimeout(() => document.addEventListener('click', close), 0);
    $$('[data-p]', menu).forEach((b) => b.onclick = async () => { menu.hidden = true; await save(); openProject(b.dataset.p); });
    $('[data-new]', menu).onclick = async () => {
      menu.hidden = true;
      const name = await promptModal('New project', 'Project name', 'My portfolio');
      if (!name) return;
      try { await save(); const d = await api('projects', { method: 'POST', body: { name } }); await openProject(d.id); } catch (e) { toast(e.message, 'error'); }
    };
    $('[data-folder]', menu).onclick = () => { menu.hidden = true; api(`projects/${enc(S.pid)}/open`, { method: 'POST', body: { what: 'project' } }).catch((e) => toast(e.message, 'error')); };
  }

  function renderSide() {
    const nav = $('#steps');
    if (!nav) return;
    const idx = STEPS.findIndex((s) => s.id === S.step);
    nav.innerHTML = `<ol>${STEPS.map((s, i) => {
      const st = stepState(s.id);
      return `<li><button class="step ${s.id === S.step ? 'active' : ''} ${st.done ? 'done' : ''}" data-step="${s.id}" ${s.id === S.step ? 'aria-current="step"' : ''}>
        <span class="num">${st.done && s.id !== S.step ? icon('check') : i + 1}</span>
        <span class="txt"><strong>${esc(s.title)}</strong><small>${esc(st.sub)}</small></span></button></li>`;
    }).join('')}</ol>
      <div class="steps-foot">
        <div class="progress-mini"><span style="width:${Math.round(STEPS.filter((s) => stepState(s.id).done).length / STEPS.length * 100)}%"></span></div>
        <p>${STEPS.filter((s) => stepState(s.id).done).length} of ${STEPS.length} steps done</p>
        <button class="link-btn" id="open-folder">${icon('folder')}Open project folder</button>
      </div>`;
    $$('[data-step]', nav).forEach((b) => b.onclick = () => go(b.dataset.step));
    $('#open-folder').onclick = () => api(`projects/${enc(S.pid)}/open`, { method: 'POST', body: { what: 'project' } }).catch((e) => toast(e.message, 'error'));
    renderSummary();
    void idx;
  }

  function renderSummary() {
    const el = $('#summary');
    if (!el) return;
    const r = room(), t = theme(r), p = S.profile;
    const img = themeImage(t);
    const lb = S.studio.last_build;
    const hero = S.outputs.hero ? projectUrl('output/hero.png') + `?v=${S.outputs.hero.mtime}` : '';
    const checks = [
      ['Name on the sign', nameCheck().level !== 'error'],
      ['At least one project picture', (p.projects || []).some((x) => x.image)],
      ['A way to contact you', Object.keys(p.links || {}).length > 0],
      ['Room and theme', !!r],
    ];
    el.innerHTML = `
      <div class="sum-card">
        <div class="sum-img">${hero && lb ? `<img src="${esc(hero)}" alt="Your latest build">` : img ? `<img src="${esc(img)}" alt="">` : `<div class="sum-empty">${icon('cube')}</div>`}
          ${hero && lb ? '<span class="tag">Latest build</span>' : r ? '<span class="tag">Room preview</span>' : ''}</div>
        <div class="sum-body">
          <h3>${esc(p.name || 'Your name')}</h3>
          <p class="muted">${esc(p.role || 'Your role or shop')}</p>
          ${r ? `<p class="sum-room">${icon('cube', 'sm')}${esc(r.name)}<span class="sw-row">${t ? swatches(t, 4) : ''}</span></p>` : ''}
        </div>
        <ul class="checks">${checks.map(([label, ok]) => `<li class="${ok ? 'ok' : ''}">${icon(ok ? 'check' : 'clock', 'sm')}${esc(label)}</li>`).join('')}</ul>
        <button class="btn primary block" id="sum-build">${S.job && S.job.state === 'running' ? `<span class="spinner light"></span>Building… ${Math.round(S.job.progress * 100)}%` : `${icon('sparkles')}${lb ? 'Build again' : 'Build my portfolio'}`}</button>
        ${lb ? `<p class="muted center small">Last build ${esc(ago(lb.when))} · ${lb.quality === 'final' ? 'Final quality' : 'Quick preview'}</p>` : ''}
      </div>
      <div class="sum-tip">${icon('info')}<p>${esc(tipFor(S.step))}</p></div>`;
    $('#sum-build').onclick = () => go('build');
  }

  function tipFor(step) {
    const per = persona();
    return {
      persona: 'Your choice only fills in suggestions. Nothing is locked - you can change the room, links and sizes later.',
      profile: 'Keep your name short so it reads well on the sign. Visitors can click the sign, mug and shelves to reach your links.',
      projects: 'Wide pictures (16:10, like a laptop screen) look best. The first project goes on the main screen.',
      room: per ? per.objects : 'Click a colour theme to see the room in different colours.',
      furnish: 'A photo of your own chair, plant or pet makes the room feel like yours. Photos taken straight on, on a plain background, work best.',
      build: 'Start with a Quick preview to check everything, then make the Final quality version to share.',
    }[step] || '';
  }

  function swatches(t, n = 5) {
    const keys = ['main', 'accent_1', 'accent_2', 'wall', 'floor', 'wood'];
    return keys.filter((k) => t.colors[k]).slice(0, n).map((k) => `<i style="background:${esc(t.colors[k])}"></i>`).join('');
  }

  function setHash(push) {
    const h = `#p=${enc(S.pid)}&s=${S.step}`;
    if (location.hash !== h) history[push ? 'pushState' : 'replaceState'](null, '', h);
  }

  // Back / Forward buttons and hand-edited addresses move between steps and projects too.
  async function onHashChange() {
    const hash = new URLSearchParams(location.hash.slice(1));
    const pid = hash.get('p');
    const step = hash.get('s');
    const leave = async () => { clearTimeout(S.saveTimer); await save().catch(() => {}); };
    try {
      if (!pid) { if (S.pid) { await leave(); S.projects = await api('projects'); renderWelcome(); } return; }
      if (pid !== S.pid) { await leave(); await openProject(pid, step); return; }
      if (step && step !== S.step) go(step, true);
    } catch (e) { toast(e.message, 'error'); }
  }
  window.addEventListener('hashchange', onHashChange);           // also fires for Back / Forward between steps

  function go(step, fromHistory) {
    if (!STEPS.some((s) => s.id === step)) return;
    S.step = step;
    S.studio.step = step;
    setHash(!fromHistory);
    changed();
    renderMain();
    renderSide();
    const m = $('#main');
    m.scrollTop = 0; window.scrollTo(0, 0);
    m.focus({ preventScroll: true });
  }

  function navButtons(prevId, nextId, nextLabel = 'Continue') {
    return `<div class="step-nav">
      ${prevId ? `<button class="btn ghost" data-go="${prevId}">${icon('left')}Back</button>` : '<span></span>'}
      ${nextId ? `<button class="btn primary" data-go="${nextId}">${esc(nextLabel)}${icon('right')}</button>` : ''}
    </div>`;
  }
  function bindNav(root) { $$('[data-go]', root).forEach((b) => b.onclick = () => go(b.dataset.go)); }

  function renderMain() {
    const el = $('#main');
    if (!el) return;
    const fn = { persona: viewPersona, profile: viewProfile, projects: viewProjects, room: viewRoom, furnish: viewFurnish, build: viewBuild }[S.step];
    fn(el);
    bindNav(el);
  }

  function header(kicker, title, lead) {
    return `<header class="view-head"><p class="kicker">${esc(kicker)}</p><h1>${esc(title)}</h1>${lead ? `<p class="lead">${lead}</p>` : ''}</header>`;
  }

  // ------------------------------------------------------------------ step 1: persona
  function viewPersona(el) {
    const cur = S.studio.persona;
    const cards = S.personas.map((p) => {
      const sug = firstRoom(p);
      return `<button class="persona ${cur === p.id ? 'selected' : ''}" data-persona="${p.id}" aria-pressed="${cur === p.id}" style="--tint:${esc(p.tint)}">
        <span class="p-icon">${icon(p.icon)}</span>
        <span class="p-text"><strong>${esc(p.label)}</strong><small>${esc(p.blurb)}</small></span>
        ${sug ? `<span class="p-room">${icon('cube', 'sm')}${esc(sug.room.name)}</span>` : ''}
        <span class="p-check">${icon('check')}</span>
      </button>`;
    }).join('');
    const per = persona();
    let plan = '';
    if (per) {
      const sug = firstRoom(per);
      const img = sug ? themeImage(sug.theme) : '';
      plan = `<section class="card plan">
        ${img ? `<img class="plan-img" src="${esc(img)}" alt="">` : ''}
        <div class="plan-body">
          <h2>Here’s what we suggest for a ${esc(per.label.toLowerCase())}</h2>
          <dl>
            <dt>Room</dt><dd>${sug ? `${esc(sug.room.name)} · ${esc(sug.theme ? sug.theme.label : '')}` : 'Any room'}</dd>
            <dt>Links</dt><dd class="chips">${per.links.map((l) => `<span class="chip">${esc((S.linkTypes[l] || {}).label || l)}</span>`).join('')}</dd>
            <dt>Picture sizes</dt><dd class="chips">${per.exports.map((x) => `<span class="chip">${esc((S.exportsInfo[x] || {}).label || x)}</span>`).join('')}</dd>
            <dt>In the room</dt><dd>${esc(per.objects)}</dd>
          </dl>
          <p class="muted small">${S.studio.touched.room ? 'You already chose a room, so we’ll keep it.' : 'You can change all of this in the next steps.'}</p>
        </div>
      </section>`;
    }
    el.innerHTML = header('Step 1 of 6', 'Who is this portfolio for?', 'Pick the closest match. We’ll suggest a room, the links people will want, and the picture sizes you’ll need.')
      + `<div class="persona-grid" role="list">${cards}</div>${plan}` + navButtons('', 'profile', per ? 'Use these suggestions' : 'Skip for now');
    $$('[data-persona]', el).forEach((b) => b.onclick = () => { applyPersona(b.dataset.persona); viewPersona(el); bindNav(el); });
    const next = $('[data-go="profile"]', el);
    if (next) next.onclick = () => go('profile');
  }

  function firstRoom(p) {
    for (const [rid, tid] of p.rooms) {
      const r = room(rid);
      if (r) return { room: r, theme: r.themes.find((t) => t.id === tid) || r.themes.find((t) => t.default) || r.themes[0] };
    }
    return null;
  }

  function applyPersona(id) {
    const p = S.personas.find((x) => x.id === id);
    if (!p) return;
    S.studio.persona = id;
    if (!S.studio.touched.room) {
      const sug = firstRoom(p);
      if (sug) { S.studio.room = sug.room.id; S.studio.theme = sug.theme ? sug.theme.id : ''; }
    }
    const order = linkRows().map((r) => r.type);
    p.links.forEach((t) => { if (!order.includes(t)) order.push(t); });
    S.studio.link_order = order;
    if (!S.studio.touched.exports) S.studio.build.exports = p.exports.slice();
    if (!S.studio.touched.brand) { S.studio.brand_color_suggest = p.tint; }
    changed();
  }

  // ------------------------------------------------------------------ step 2: profile
  function viewProfile(el) {
    const p = S.profile, per = persona();
    const t = theme();
    const brand = S.profile.brand_color || S.studio.brand_color_suggest || (t && t.colors.accent_1) || '#5B4CF0';
    const roomColors = t ? ['main', 'accent_1', 'accent_2', 'accent_3'].map((k) => t.colors[k]).filter(Boolean) : [];
    el.innerHTML = header('Step 2 of 6', 'Your details', 'This goes on the sign in your room and at the top of your website.') + `
      <section class="card form-card">
        <h2 class="card-title">${icon('idcard')}The basics</h2>
        <div class="grid2">
          <div class="field">
            <label for="f-name">Your name <span class="req">required</span></label>
            <input id="f-name" maxlength="60" autocomplete="name" value="${esc(p.name)}" placeholder="${esc(per && per.id === 'shop' ? 'Your shop name' : 'Alex Rivera')}" aria-describedby="f-name-msg">
            <div class="counter-row"><p class="msg" id="f-name-msg" aria-live="polite"></p><span class="counter" id="f-name-count"></span></div>
          </div>
          <div class="field">
            <label for="f-role">What you do</label>
            <input id="f-role" maxlength="80" value="${esc(p.role)}" placeholder="${esc(per ? per.role : 'Front-end Developer')}" aria-describedby="f-role-msg">
            <div class="counter-row"><p class="msg" id="f-role-msg" aria-live="polite"></p><span class="counter" id="f-role-count"></span></div>
          </div>
        </div>
        <div class="field">
          <label for="f-tag">One line about you <span class="opt">shown on your website</span></label>
          <textarea id="f-tag" rows="2" maxlength="160" placeholder="${esc(per ? per.taglines[0] : 'I build friendly, fast web apps.')}">${esc(p.tagline)}</textarea>
          ${per ? `<div class="suggest"><span>Ideas:</span>${per.taglines.map((x, i) => `<button class="chip btnchip" data-tag="${i}">${esc(x)}</button>`).join('')}</div>` : ''}
        </div>
      </section>

      <section class="card form-card">
        <h2 class="card-title">${icon('link')}Links</h2>
        <p class="muted">Visitors click things in your room to reach you. Links that aren’t on an object appear at the top of your website.</p>
        <div id="links" class="links"></div>
        <div class="add-links" id="add-links"></div>
      </section>

      <section class="card form-card">
        <h2 class="card-title">${icon('star')}Skills or highlights <span class="opt">optional</span></h2>
        <div class="tags" id="tags"></div>
        <input id="f-skill" placeholder="Type one and press Enter" maxlength="40" aria-label="Add a skill">
        ${per ? `<div class="suggest"><span>Add:</span>${per.skills.map((x) => `<button class="chip btnchip" data-skill="${esc(x)}">${icon('plus', 'sm')}${esc(x)}</button>`).join('')}</div>` : ''}
      </section>

      <section class="card form-card">
        <h2 class="card-title">${icon('brush')}Brand colour <span class="opt">optional</span></h2>
        <label class="switch"><input type="checkbox" id="brand-on" ${S.studio.brand_on ? 'checked' : ''}><span class="track"></span><span>Use my own colour for signs, glow and buttons</span></label>
        <div class="brand-row ${S.studio.brand_on ? '' : 'disabled'}" id="brand-row">
          <input type="color" id="brand" value="${esc(brand)}" aria-label="Brand colour">
          <input id="brand-hex" class="hex" value="${esc(brand.toUpperCase())}" maxlength="7" aria-label="Brand colour hex code">
          ${roomColors.length ? `<span class="muted small">Room colours:</span>${roomColors.map((c) => `<button class="swatch-btn" data-color="${esc(c)}" style="background:${esc(c)}" aria-label="Use ${esc(c)}"></button>`).join('')}` : ''}
        </div>
      </section>
      <div class="inline-actions"><button class="link-btn" id="load-sample">${icon('sparkles')}Fill everything with the example profile</button></div>
      ${navButtons('persona', 'projects')}`;

    const name = $('#f-name', el), role = $('#f-role', el);
    const upd = () => {
      showMsg('#f-name-msg', nameCheck(), name);
      showMsg('#f-role-msg', roleCheck(), role);
      const ln = signLimits('name'), lr = signLimits('role');
      $('#f-name-count').textContent = `${(p.name || '').length} / ${ln.fit}`;
      $('#f-name-count').className = 'counter ' + ((p.name || '').length > ln.max ? 'bad' : (p.name || '').length > ln.fit ? 'warnc' : '');
      $('#f-role-count').textContent = `${(p.role || '').length} / ${lr.fit}`;
      $('#f-role-count').className = 'counter ' + ((p.role || '').length > lr.max ? 'bad' : (p.role || '').length > lr.fit ? 'warnc' : '');
    };
    name.oninput = () => { p.name = name.value; upd(); changed(); };
    role.oninput = () => { p.role = role.value; upd(); changed(); };
    $('#f-tag', el).oninput = (e) => { p.tagline = e.target.value; changed(); };
    $$('[data-tag]', el).forEach((b) => b.onclick = () => { p.tagline = per.taglines[+b.dataset.tag]; $('#f-tag').value = p.tagline; changed(); });
    upd();
    renderLinks();
    renderTags();
    const skill = $('#f-skill', el);
    skill.onkeydown = (e) => {
      if (e.key === 'Enter' || e.key === ',') {
        e.preventDefault();
        addSkill(skill.value);
        skill.value = '';
      } else if (e.key === 'Backspace' && !skill.value && p.skills.length) { p.skills.pop(); renderTags(); changed(); }
    };
    skill.onblur = () => { if (skill.value.trim()) { addSkill(skill.value); skill.value = ''; } };
    $$('[data-skill]', el).forEach((b) => b.onclick = () => addSkill(b.dataset.skill));
    const on = $('#brand-on', el), picker = $('#brand', el), hex = $('#brand-hex', el);
    const setColor = (c) => { picker.value = c; hex.value = c.toUpperCase(); if (S.studio.brand_on) { p.brand_color = c.toUpperCase(); } S.studio.touched.brand = true; changed(); };
    on.onchange = () => { S.studio.brand_on = on.checked; p.brand_color = on.checked ? picker.value.toUpperCase() : ''; $('#brand-row').classList.toggle('disabled', !on.checked); changed(); };
    picker.oninput = () => setColor(picker.value);
    hex.oninput = () => { if (/^#[0-9a-f]{6}$/i.test(hex.value)) setColor(hex.value); };
    $$('[data-color]', el).forEach((b) => b.onclick = () => { if (!S.studio.brand_on) { on.checked = true; on.onchange(); } setColor(b.dataset.color); });
    $('#load-sample', el).onclick = async () => {
      if ((p.name || (p.projects || []).length) && !(await confirmModal('Replace your details?', 'This fills in the example name, links and four sample projects. Your current details will be replaced.', 'Use the example'))) return;
      try {
        await save();
        const d = await api(`projects/${enc(S.pid)}/sample`, { method: 'POST' });
        S.profile = Object.assign(S.profile, d.profile);
        S.studio.link_order = Object.keys(d.profile.links || {});
        changed();
        viewProfile(el); bindNav(el);
        toast('Example profile loaded.', 'ok');
      } catch (e) { toast(e.message, 'error'); }
    };
  }

  function showMsg(sel, check, input) {
    const m = $(sel);
    if (!m) return;
    m.textContent = check.msg || '';
    m.className = 'msg ' + (check.level || '');
    if (input) input.setAttribute('aria-invalid', check.level === 'error' && input.value ? 'true' : 'false');
  }

  function addSkill(v) {
    v = (v || '').replace(/,/g, '').trim();
    if (!v) return;
    S.profile.skills = S.profile.skills || [];
    if (S.profile.skills.length >= 12) return toast('That’s plenty! Up to 12 skills fit.', 'info');
    if (!S.profile.skills.some((s) => s.toLowerCase() === v.toLowerCase())) S.profile.skills.push(v.slice(0, 40));
    renderTags(); changed();
  }
  function renderTags() {
    const el = $('#tags');
    if (!el) return;
    el.innerHTML = (S.profile.skills || []).map((s, i) => `<span class="tag-chip">${esc(s)}<button aria-label="Remove ${esc(s)}" data-rm="${i}">${icon('x', 'sm')}</button></span>`).join('')
      || '<span class="muted small">No skills yet.</span>';
    $$('[data-rm]', el).forEach((b) => b.onclick = () => { S.profile.skills.splice(+b.dataset.rm, 1); renderTags(); changed(); });
  }

  function renderLinks() {
    const box = $('#links');
    if (!box) return;
    const rows = linkRows();
    const r = room();
    const inRoom = new Set(r && r.hooks ? r.hooks.links : ['email', 'website', 'github', 'linkedin']);
    box.innerHTML = rows.map((row, i) => {
      const info = S.linkTypes[row.type] || { label: row.type };
      const v = validateLink(row.type, row.value);
      const where = inRoom.has(row.type) && info.room ? `<span class="where" title="Visitors click the ${esc(info.room.toLowerCase())} in your room to open this">${icon('cube', 'sm')}${esc(info.room)}</span>` : '<span class="where web" title="Shown at the top of your website">On your website</span>';
      return `<div class="link-row" data-i="${i}">
        <label class="lr-type" for="lk-${i}">${esc(info.label)}</label>
        <div class="lr-input">
          <input id="lk-${i}" value="${esc(row.value)}" placeholder="${esc(info.placeholder || 'https://')}" inputmode="${row.type === 'email' ? 'email' : 'url'}" aria-describedby="lk-${i}-msg" aria-invalid="${v.level === 'error'}">
          <span class="lr-state ${v.level}">${v.level === 'ok' ? icon('check', 'sm') : v.level === 'error' ? icon('alert', 'sm') : ''}</span>
        </div>
        ${where}
        <button class="icon-btn" data-rmlink="${i}" aria-label="Remove ${esc(info.label)} link">${icon('trash')}</button>
        <p class="msg ${v.level === 'error' ? 'error' : ''}" id="lk-${i}-msg">${esc(v.level === 'error' ? v.msg : '')}</p>
      </div>`;
    }).join('') || '<p class="muted small">No links yet. Add at least an email so people can reach you.</p>';
    $$('.link-row', box).forEach((rowEl) => {
      const i = +rowEl.dataset.i;
      const input = $('input', rowEl);
      input.oninput = () => {
        const rs = linkRows(); rs[i].value = input.value; setLinkRows(rs); changed();
        const v = validateLink(rs[i].type, input.value);
        const st = $('.lr-state', rowEl);
        st.className = 'lr-state ' + (v.level === 'ok' ? 'ok' : '');
        st.innerHTML = v.level === 'ok' ? icon('check', 'sm') : '';
        if (v.level !== 'error') { $('.msg', rowEl).textContent = ''; input.setAttribute('aria-invalid', 'false'); }
      };
      input.onblur = () => {
        const rs = linkRows(); const tidy = tidyLink(rs[i].type, input.value);
        if (tidy !== input.value) { input.value = tidy; }
        rs[i].value = tidy; setLinkRows(rs); changed();
        const v = validateLink(rs[i].type, tidy);
        $('.msg', rowEl).textContent = v.level === 'error' ? v.msg : '';
        $('.msg', rowEl).className = 'msg ' + (v.level === 'error' ? 'error' : '');
        const st = $('.lr-state', rowEl);
        st.className = 'lr-state ' + v.level; st.innerHTML = v.level === 'ok' ? icon('check', 'sm') : v.level === 'error' ? icon('alert', 'sm') : '';
        input.setAttribute('aria-invalid', v.level === 'error');
      };
    });
    $$('[data-rmlink]', box).forEach((b) => b.onclick = () => { const rs = linkRows(); rs.splice(+b.dataset.rmlink, 1); setLinkRows(rs); changed(); renderLinks(); });
    const used = new Set(rows.map((x) => x.type));
    const per = persona();
    const suggested = (per ? per.links : ['email', 'website', 'linkedin', 'instagram']).filter((t) => !used.has(t));
    const others = Object.keys(S.linkTypes).filter((t) => !used.has(t) && !suggested.includes(t));
    $('#add-links').innerHTML = (suggested.length ? `<span class="muted small">Add:</span>${suggested.map((t) => `<button class="chip btnchip" data-add="${t}">${icon('plus', 'sm')}${esc(S.linkTypes[t].label)}</button>`).join('')}` : '')
      + (others.length ? `<select id="more-links" aria-label="Add another kind of link"><option value="">More link types…</option>${others.map((t) => `<option value="${t}">${esc(S.linkTypes[t].label)}</option>`).join('')}</select>` : '');
    const addType = (t) => { const rs = linkRows(); rs.push({ type: t, value: '' }); setLinkRows(rs); changed(); renderLinks(); const inp = $(`#lk-${rs.length - 1}`); if (inp) inp.focus(); };
    $$('[data-add]').forEach((b) => b.onclick = () => addType(b.dataset.add));
    const more = $('#more-links');
    if (more) more.onchange = () => { if (more.value) addType(more.value); };
  }

  // ------------------------------------------------------------------ step 3: projects
  function viewProjects(el) {
    const per = persona();
    const r = room();
    const spots = r && r.hooks ? r.hooks.pictures : 0;
    el.innerHTML = header('Step 3 of 6', 'Your projects', 'Add pictures of your work. They appear on the screens, frames and posters in your room, and as cards on your website.') + `
      <div class="proj-hint">${icon('info')}<span>${spots ? `The ${esc(r.name)} has <b>${spots} picture spots</b>. ` : ''}Add 3–6 projects for the best look. Drag the handle to change the order - the first one goes on the main screen.</span></div>
      <ol class="projects" id="projects"></ol>
      <div class="dropzone big" id="proj-drop" tabindex="0" role="button" aria-label="Add projects: drop pictures here or press to choose files">
        ${icon('upload')}<div><strong>Drop pictures here to add projects</strong><span>or click to choose · JPG, PNG, WebP or iPhone photos</span></div>
        <input type="file" id="proj-files" accept="image/*,.heic,.heif" multiple hidden>
      </div>
      <div class="inline-actions"><button class="btn ghost" id="add-empty">${icon('plus')}Add a project without a picture</button></div>
      ${per ? `<section class="card ideas"><h2 class="card-title">${icon('sparkles')}Not sure what to show?</h2><p class="muted">Ideas for a ${esc(per.label.toLowerCase())}:</p><ul>${per.project_ideas.map((x) => `<li>${esc(x)}</li>`).join('')}</ul></section>` : ''}
      ${navButtons('profile', 'room')}`;
    renderProjectList();
    const drop = $('#proj-drop', el), files = $('#proj-files', el);
    drop.onclick = () => files.click();
    drop.onkeydown = (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); files.click(); } };
    files.onchange = () => { addProjectFiles(Array.from(files.files)); files.value = ''; };
    dropTarget(drop, (fs) => addProjectFiles(fs));
    $('#add-empty', el).onclick = () => { S.profile.projects.push({ title: '', image: '', url: '', description: '' }); changed(); renderProjectList(); focusLastProject(); };
  }

  function focusLastProject() { const ins = $$('#projects .p-title'); if (ins.length) ins[ins.length - 1].focus(); }

  async function addProjectFiles(fs) {
    const pics = fs.filter((f) => /^image\//.test(f.type) || /\.(heic|heif|png|jpe?g|webp)$/i.test(f.name));
    if (!pics.length) return toast('Those files aren’t pictures. Use JPG, PNG or WebP.', 'error');
    for (const f of pics) {
      try {
        const up = await uploadFile(f, 'images');
        S.profile.projects.push({ title: prettyName(f.name), image: up.path, url: '', description: '' });
        changed(); renderProjectList();
      } catch (e) { toast(e.message, 'error'); }
    }
    focusLastProject();
  }

  const prettyName = (n) => n.replace(/\.[^.]+$/, '').replace(/[_-]+/g, ' ').replace(/^project /i, '').replace(/\b\w/g, (c) => c.toUpperCase()).slice(0, 60);

  async function uploadFile(file, kind) {
    if (file.size > 300 * 1024 * 1024) throw new Error('That file is too big (over 300 MB).');
    const res = await fetch(`/api/projects/${enc(S.pid)}/upload?kind=${kind}&name=${enc(file.name)}`, { method: 'POST', headers: { 'X-RoomKit-Token': TOKEN }, body: file });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(data.error || 'That file couldn’t be added.');
    return data;
  }

  function dropTarget(el, onFiles) {
    let depth = 0;
    el.addEventListener('dragenter', (e) => { if (hasFiles(e)) { depth++; el.classList.add('over'); e.preventDefault(); } });
    el.addEventListener('dragover', (e) => { if (hasFiles(e)) { e.preventDefault(); e.dataTransfer.dropEffect = 'copy'; } });
    el.addEventListener('dragleave', () => { depth = Math.max(0, depth - 1); if (!depth) el.classList.remove('over'); });
    el.addEventListener('drop', (e) => { if (!hasFiles(e)) return; e.preventDefault(); e.stopPropagation(); depth = 0; el.classList.remove('over'); onFiles(Array.from(e.dataTransfer.files)); });
  }
  const hasFiles = (e) => e.dataTransfer && Array.from(e.dataTransfer.types || []).includes('Files');

  function renderProjectList() {
    const list = $('#projects');
    if (!list) return;
    const prs = S.profile.projects || [];
    list.innerHTML = prs.map((pr, i) => `
      <li class="proj-card" data-i="${i}">
        <div class="pc-handle" title="Drag to reorder" aria-hidden="true">${icon('grip')}</div>
        <div class="pc-img dropzone ${pr.image ? 'has' : ''}" tabindex="0" role="button" aria-label="${pr.image ? 'Change' : 'Add'} the picture for ${esc(pr.title || 'this project')}">
          ${pr.image ? `<img src="${esc(projectUrl(pr.image))}" alt="">` : `${icon('image')}<span>Drop a picture</span>`}
          ${i === 0 ? '<span class="badge main-screen">Main screen</span>' : ''}
          <input type="file" accept="image/*,.heic,.heif" hidden>
        </div>
        <div class="pc-fields">
          <input class="p-title" value="${esc(pr.title)}" placeholder="Project title" maxlength="80" aria-label="Project title">
          <textarea class="p-desc" rows="2" maxlength="400" placeholder="One or two sentences about it" aria-label="Project description">${esc(pr.description)}</textarea>
          <div class="p-url-row">${icon('link', 'sm')}<input class="p-url" value="${esc(pr.url)}" placeholder="Link (optional) - https://…" aria-label="Project link"></div>
          <p class="msg p-msg"></p>
        </div>
        <div class="pc-actions">
          <button class="icon-btn" data-mv="-1" ${i === 0 ? 'disabled' : ''} aria-label="Move up">${icon('up')}</button>
          <button class="icon-btn" data-mv="1" ${i === prs.length - 1 ? 'disabled' : ''} aria-label="Move down">${icon('down')}</button>
          <button class="icon-btn danger" data-del aria-label="Remove project">${icon('trash')}</button>
        </div>
      </li>`).join('');
    $$('.proj-card', list).forEach((card) => {
      const i = +card.dataset.i;
      const pr = prs[i];
      $('.p-title', card).oninput = (e) => { pr.title = e.target.value; changed(); };
      $('.p-desc', card).oninput = (e) => { pr.description = e.target.value; changed(); };
      const url = $('.p-url', card);
      url.oninput = () => { pr.url = url.value; changed(); };
      url.onblur = () => {
        pr.url = tidyLink('website', url.value); url.value = pr.url; changed();
        const v = validateLink('website', pr.url); const m = $('.p-msg', card); m.textContent = v.level === 'error' ? v.msg : ''; m.className = 'msg p-msg ' + (v.level === 'error' ? 'error' : '');
      };
      const imgBox = $('.pc-img', card), fileIn = $('input[type=file]', imgBox);
      imgBox.onclick = () => fileIn.click();
      imgBox.onkeydown = (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); fileIn.click(); } };
      const setImg = async (f) => {
        if (!f) return;
        try { const up = await uploadFile(f, 'images'); pr.image = up.path; if (!pr.title) pr.title = prettyName(f.name); changed(); renderProjectList(); }
        catch (e) { toast(e.message, 'error'); }
      };
      fileIn.onchange = () => setImg(fileIn.files[0]);
      dropTarget(imgBox, (fs) => setImg(fs[0]));
      const img = $('img', imgBox);
      if (img) img.onload = () => {
        const ratio = img.naturalWidth / img.naturalHeight;
        if (ratio < 1.2 || ratio > 2.1) $('.p-msg', card).innerHTML = `${icon('info', 'sm')} This picture will be cropped to fit wide screens (16:10). Wide pictures look best.`;
        $('.p-msg', card).className = 'msg p-msg note';
      };
      $$('[data-mv]', card).forEach((b) => b.onclick = () => moveProject(i, i + +b.dataset.mv));
      $('[data-del]', card).onclick = () => { prs.splice(i, 1); changed(); renderProjectList(); };
      // drag to reorder (only from the handle, so typing in the fields still works)
      const handle = $('.pc-handle', card);
      handle.onmousedown = () => { card.draggable = true; };
      card.addEventListener('dragstart', (e) => { if (!card.draggable) return; e.dataTransfer.setData('text/x-roomkit-project', String(i)); e.dataTransfer.effectAllowed = 'move'; card.classList.add('dragging'); });
      card.addEventListener('dragend', () => { card.draggable = false; card.classList.remove('dragging'); $$('.proj-card').forEach((c) => c.classList.remove('drop-before', 'drop-after')); });
      card.addEventListener('dragover', (e) => {
        if (!Array.from(e.dataTransfer.types).includes('text/x-roomkit-project')) return;
        e.preventDefault();
        const rect = card.getBoundingClientRect();
        const after = e.clientY > rect.top + rect.height / 2;
        card.classList.toggle('drop-after', after); card.classList.toggle('drop-before', !after);
      });
      card.addEventListener('dragleave', () => card.classList.remove('drop-before', 'drop-after'));
      card.addEventListener('drop', (e) => {
        const from = e.dataTransfer.getData('text/x-roomkit-project');
        if (from === '') return;
        e.preventDefault();
        const after = card.classList.contains('drop-after');
        let to = i + (after ? 1 : 0);
        if (+from < to) to -= 1;
        moveProject(+from, to);
      });
    });
    renderSide();
  }

  function moveProject(from, to) {
    const prs = S.profile.projects;
    if (to < 0 || to >= prs.length || from === to) return;
    const [x] = prs.splice(from, 1);
    prs.splice(to, 0, x);
    changed(); renderProjectList();
    const btn = $(`.proj-card[data-i="${to}"] .p-title`); if (btn) btn.focus();
  }

  // ------------------------------------------------------------------ step 4: room gallery
  function viewRoom(el) {
    const per = persona();
    const filters = [['for-you', per ? `For a ${per.label.toLowerCase()}` : 'Suggested'], ['all', 'All rooms'], ['themed', 'Themed rooms']];
    let list = S.rooms.slice();
    if (S.roomFilter === 'themed') list = list.filter((r) => r.themed);
    if (S.roomFilter === 'for-you') {
      const pid = per ? per.id : 'student';
      const order = per ? per.rooms.map((x) => x[0]) : [];
      list = list.filter((r) => r.personas.includes(pid) || order.includes(r.id));
      list.sort((a, b) => (order.indexOf(a.id) + 1 || 99) - (order.indexOf(b.id) + 1 || 99));
      if (!list.length) list = S.rooms.slice();
    }
    const cur = S.studio.room;
    if (cur && !list.some((r) => r.id === cur) && room(cur)) list.unshift(room(cur));
    const cards = list.map((r) => {
      const sel = r.id === cur;
      const t = sel ? theme(r) : (r.themes.find((x) => x.default) || r.themes[0]);
      const img = themeImage(t);
      return `<article class="room-card ${sel ? 'selected' : ''}" data-room="${r.id}">
        <button class="rc-pick" data-pick="${r.id}" aria-pressed="${sel}" aria-label="Choose the ${esc(r.name)}">
          <span class="rc-img" style="${t ? `background:linear-gradient(135deg, ${esc(t.colors.wall || '#eee')}, ${esc(t.colors.floor || '#ddd')})` : ''}">
            ${img ? `<img src="${esc(img)}" alt="" loading="lazy">` : `<span class="rc-soon">${icon('cube')}Preview coming soon</span>`}
            ${r.themed ? '<span class="badge new">New · Themed</span>' : ''}
            ${sel ? `<span class="badge chosen">${icon('check', 'sm')}Your room</span>` : ''}
          </span>
        </button>
        <div class="rc-body">
          <div class="rc-head"><h3>${esc(r.name)}</h3>${r.hooks ? `<span class="muted small">${r.hooks.pictures} pictures · ${r.slots.length} furniture spots</span>` : ''}</div>
          <p class="muted">${esc(r.blurb)}</p>
          <div class="rc-personas">${r.personas.slice(0, 4).map((pid) => { const p = S.personas.find((x) => x.id === pid); return p ? `<span class="pbadge" style="--tint:${esc(p.tint)}">${icon(p.icon, 'sm')}${esc(shortLabel(p))}</span>` : ''; }).join('')}</div>
          <div class="themes" role="group" aria-label="Colour themes for ${esc(r.name)}">
            ${r.themes.map((th) => `<button class="theme-btn ${sel && t && th.id === t.id ? 'on' : ''}" data-room="${r.id}" data-theme="${th.id}" aria-pressed="${sel && t && th.id === t.id}">
              <span class="sw">${swatches(th, 3)}</span>${esc(th.label)}</button>`).join('')}
          </div>
        </div>
      </article>`;
    }).join('');
    const r = room();
    el.innerHTML = header('Step 4 of 6', 'Choose your room', 'Every room is furnished with pieces modelled on real furniture. Pick one, then a colour theme.') + `
      <div class="filters" role="tablist">${filters.map(([id, label]) => `<button role="tab" class="filter ${S.roomFilter === id ? 'on' : ''}" aria-selected="${S.roomFilter === id}" data-filter="${id}">${esc(label)}</button>`).join('')}
        ${S.roomsScanning ? `<span class="scan">${icon('refresh', 'sm spin')}Checking rooms…</span>` : ''}</div>
      <div class="room-grid">${cards || '<p class="muted">No rooms found in templates/.</p>'}</div>
      ${r ? `<section class="card seed-card"><div><h2 class="card-title">${icon('dice')}Shuffle the little things</h2><p class="muted">Books, bottles, plants and props are arranged differently for each number, so your room won’t look like anyone else’s.</p></div>
        <div class="seed-ctl"><button class="icon-btn" id="seed-dn" aria-label="Previous arrangement">${icon('left')}</button><output id="seed-val" aria-live="polite">Arrangement #${esc(S.studio.seed || 1)}</output><button class="icon-btn" id="seed-up" aria-label="Next arrangement">${icon('right')}</button><button class="btn ghost" id="seed-rand">${icon('dice')}Surprise me</button></div></section>` : ''}
      ${navButtons('projects', 'furnish')}`;
    $$('[data-filter]', el).forEach((b) => b.onclick = () => { S.roomFilter = b.dataset.filter; viewRoom(el); bindNav(el); });
    const pick = (rid, tid) => {
      const rr = room(rid);
      const changedRoom = S.studio.room !== rid;
      S.studio.room = rid;
      S.studio.theme = tid || (rr.themes.find((x) => x.default) || rr.themes[0] || {}).id || '';
      S.studio.touched.room = true;
      if (changedRoom && (S.studio.swaps || []).length) {
        const keep = S.studio.swaps.filter((s) => rr.slots.some((x) => x.name === s.slot));
        if (keep.length !== S.studio.swaps.length) toast(`${S.studio.swaps.length - keep.length} furniture swap(s) don’t fit this room and were set aside.`, 'info');
        S.studio.swaps = keep;
      }
      changed(); viewRoom(el); bindNav(el);
    };
    $$('[data-pick]', el).forEach((b) => b.onclick = () => pick(b.dataset.pick, S.studio.room === b.dataset.pick ? S.studio.theme : ''));
    $$('[data-theme]', el).forEach((b) => b.onclick = () => pick(b.dataset.room, b.dataset.theme));
    const setSeed = (n) => { S.studio.seed = Math.max(1, Math.min(9999, n)); $('#seed-val').textContent = `Arrangement #${S.studio.seed}`; changed(); };
    if (r) {
      $('#seed-dn').onclick = () => setSeed((S.studio.seed || 1) - 1);
      $('#seed-up').onclick = () => setSeed((S.studio.seed || 1) + 1);
      $('#seed-rand').onclick = () => setSeed(1 + Math.floor(Math.random() * 999));
    }
  }
  const shortLabel = (p) => ({ designer: 'Designers', artist: 'Artists', shop: 'Shops', streamer: 'Streamers', student: 'Students', writer: 'Writers', teacher: 'Teachers', couple: 'Couples & gifts' }[p.id] || p.label);

  // ------------------------------------------------------------------ step 5: make it yours
  function viewFurnish(el) {
    const r = room();
    if (!r) {
      el.innerHTML = header('Step 5 of 6', 'Make it yours', '') + `<div class="empty">${icon('cube')}<h2>Choose a room first</h2><p>Then you can swap its furniture for your own.</p><button class="btn primary" data-go="room">Choose a room</button></div>`;
      return;
    }
    const keys = S.status.keys || {};
    const anyKey = keys.meshy?.set || keys.fal?.set || keys.hf?.set;
    const feats = S.status.features || {};
    const t = theme(r);
    el.innerHTML = header('Step 5 of 6', 'Make it yours', 'Swap any piece of furniture for your own - drop a photo of your chair, plant or pet, or a 3D model. This step is optional.') + `
      <div class="furnish-top card">
        ${themeImage(t) ? `<img src="${esc(themeImage(t))}" alt="">` : ''}
        <div>
          <h2>${esc(r.name)} · ${esc(t ? t.label : '')}</h2>
          <div class="ways">
            <div class="way">${icon('sparkles')}<div><strong>AI 3D model</strong><span>Best look. Needs a free or paid key from an AI service. About 1–3 minutes per piece.</span></div></div>
            <div class="way">${icon('cube')}<div><strong>Quick blocky version</strong><span>Free and instant. Built from simple shapes in your photo’s colours.</span></div></div>
          </div>
          <p class="key-state ${anyKey ? 'ok' : ''}">${icon(anyKey ? 'check' : 'key', 'sm')}${anyKey ? `AI key saved (${['meshy', 'fal', 'hf'].filter((k) => keys[k]?.set).map((k) => ({ meshy: 'Meshy', fal: 'fal', hf: 'Hugging Face' }[k])).join(', ')})` : 'No AI key yet - blocky versions work without one.'}
            <button class="link-btn" id="keys-btn">${anyKey ? 'Manage keys' : 'Add a key'}</button></p>
          ${feats.photo_to_3d === false && S.status.blender.state === 'ok' ? `<p class="muted small">${icon('info', 'sm')} AI models from photos arrive with the next kit update. Until then photos are built as blocky versions, and 3D model files work already.</p>` : ''}
        </div>
      </div>
      <ul class="slots" id="slots">${r.slots.map((s) => slotRow(s)).join('')}</ul>
      ${navButtons('room', 'build')}`;
    $('#keys-btn', el).onclick = () => openSettings('keys');
    bindSlots(el, r);
  }

  function slotRow(s) {
    const sw = (S.studio.swaps || []).find((x) => x.slot === s.name);
    const open = S.openSlot === s.name;
    const size = s.size ? `${s.size[0].toFixed(2)} × ${s.size[1].toFixed(2)} × ${s.size[2].toFixed(2)} m` : '';
    return `<li class="slot ${sw ? 'swapped' : ''} ${open ? 'open' : ''}" data-slot="${esc(s.name)}">
      <div class="slot-head">
        <span class="slot-icon ${sw && sw.kind !== 'model' ? 'photo' : ''}">${sw && sw.kind !== 'model' ? `<img src="${esc(projectUrl(sw.file))}" alt="">` : icon(SLOT_ICON[s.name] || 'cube')}</span>
        <div class="slot-text"><strong>${esc(s.label)}</strong><small>${sw ? esc(swapSummary(sw)) : `${esc(s.hint)}${s.where ? ' · ' + esc(s.where) : ''}${size ? ` · <span class="nowrap">${size}</span>` : ''}`}</small></div>
        ${sw ? `<span class="status-pill on">${icon('check', 'sm')}Your own</span>` : `<span class="status-pill">Room’s own</span>`}
        <button class="btn ${sw || open ? 'ghost' : 'soft'} sm" data-toggle aria-expanded="${open}" aria-label="${esc((open ? 'Done with ' : sw ? 'Edit your own ' : 'Use your own ') + s.label.toLowerCase())}">${open ? 'Done' : sw ? 'Edit' : 'Use my own'}</button>
      </div>
      ${open ? slotEditor(s, sw) : ''}
    </li>`;
  }

  function swapSummary(sw) {
    const prov = { auto: 'automatic', meshy: 'Meshy', fal: 'fal.ai', hf: 'Hugging Face', sample: 'demo model' }[sw.provider || 'auto'];
    const how = sw.kind === 'model' ? 'Your 3D model' : sw.method === 'ai' ? `Your photo → AI 3D model (${prov})` : 'Your photo → quick blocky version';
    const extra = [];
    if (Number(sw.turn)) extra.push(`turned ${sw.turn}°`);
    if (sw.scale && Math.abs(sw.scale - 1) > 0.01) extra.push(`${Math.round(sw.scale * 100)}% size`);
    if (sw.colors && sw.colors !== 'match') extra.push(sw.colors === 'original' ? 'original colours' : 'room colours');
    return how + (extra.length ? ' · ' + extra.join(' · ') : '');
  }

  function slotEditor(s, sw) {
    const feats = S.status.features || {};
    const providers = [['auto', 'Automatic (uses your saved key)'], ['meshy', 'Meshy'], ['fal', 'fal.ai (pay per model)'], ['hf', 'Hugging Face (free, best effort)'], ['sample', 'Demo model (no key, to try it out)']]
      .filter(([id]) => !feats.providers || !feats.providers.length || feats.providers.includes(id) || !feats.photo_to_3d);
    if (!sw) {
      return `<div class="slot-body">
        <div class="dropzone slot-drop" tabindex="0" role="button" aria-label="Drop a photo or 3D model for the ${esc(s.label)}">
          ${icon('upload')}<div><strong>Drop a photo or a 3D model</strong><span>Photo: JPG, PNG, iPhone · Model: .glb, .obj, .fbx, .stl</span></div>
          <input type="file" accept="image/*,.heic,.heif,.glb,.gltf,.obj,.fbx,.stl" hidden>
        </div>
      </div>`;
    }
    const isPhoto = sw.kind !== 'model';
    const turn = Number(sw.turn || 0);
    return `<div class="slot-body">
      <div class="swap-grid">
        <div class="swap-preview">
          ${isPhoto ? `<img src="${esc(projectUrl(sw.file))}" alt="Your photo for the ${esc(s.label)}">` : `<div class="model-file">${icon('cube')}<span>${esc(sw.name || sw.file.split('/').pop())}</span></div>`}
          <button class="link-btn" data-replace>${icon('refresh', 'sm')}Replace file</button>
          <input type="file" accept="image/*,.heic,.heif,.glb,.gltf,.obj,.fbx,.stl" hidden>
        </div>
        <div class="swap-opts">
          ${isPhoto ? `<fieldset class="method"><legend>How should we make it?</legend>
            <label class="radio-card ${sw.method === 'ai' ? 'on' : ''}"><input type="radio" name="m-${esc(s.name)}" value="ai" ${sw.method === 'ai' ? 'checked' : ''}><span>${icon('sparkles')}<strong>AI 3D model</strong><em class="best">Best</em><small>Needs a free or paid key. 1–3 min.</small></span></label>
            <label class="radio-card ${sw.method !== 'ai' ? 'on' : ''}"><input type="radio" name="m-${esc(s.name)}" value="blocky" ${sw.method !== 'ai' ? 'checked' : ''}><span>${icon('cube')}<strong>Quick blocky version</strong><em class="free">Free</em><small>Instant, simple shapes.</small></span></label>
          </fieldset>
          ${sw.method === 'ai' ? `<div class="field inline"><label for="prov-${esc(s.name)}">AI service</label><select id="prov-${esc(s.name)}" data-provider>${providers.map(([id, l]) => `<option value="${id}" ${sw.provider === id ? 'selected' : ''}>${esc(l)}</option>`).join('')}</select></div>
            <p class="muted small">${icon('info', 'sm')} Meshy and fal charge per model (about $0.02–0.60). Free Meshy models are licensed CC BY, so credit Meshy on your site. The result is reused when you rebuild, so you only pay once.</p>` : ''}` : `<p class="muted">${icon('info', 'sm')} Your 3D model will be scaled to fit this spot and recoloured to match the room (you can keep its own colours below).</p>`}
          <div class="tune">
            <span class="flabel">Turn it</span>
            <div class="tune-ctl"><div class="seg" role="group" aria-label="Turn">${[0, 90, 180, 270].map((d) => `<button class="${turn === d ? 'on' : ''}" data-turn="${d}" aria-pressed="${turn === d}">${d}°</button>`).join('')}</div>
              <input type="range" min="-180" max="180" step="5" value="${turn > 180 ? turn - 360 : turn}" data-turnfine aria-label="Fine turn in degrees"><output data-turnout>${turn}°</output></div>
            <label class="flabel" for="sc-${esc(s.name)}">Size</label>
            <div class="tune-ctl"><input id="sc-${esc(s.name)}" type="range" min="50" max="150" step="5" value="${Math.round((sw.scale || 1) * 100)}" data-scale ${feats.furniture_scale === false ? 'disabled' : ''}><output data-scaleout>${Math.round((sw.scale || 1) * 100)}%</output>
            ${feats.furniture_scale === false ? '<span class="muted small">Resizing arrives with the next kit update.</span>' : ''}</div>
            <span class="flabel">Colours</span>
            <div class="tune-ctl"><div class="seg" role="group" aria-label="Colours">${[['match', 'Match the room'], ['palette', 'Room colours only'], ['original', 'Keep original']].map(([id, l]) => `<button class="${(sw.colors || 'match') === id ? 'on' : ''}" data-colors="${id}" aria-pressed="${(sw.colors || 'match') === id}">${esc(l)}</button>`).join('')}</div></div>
          </div>
          <button class="btn ghost danger sm remove" data-remove>${icon('trash')}Use the room’s own ${esc(s.label.toLowerCase())}</button>
        </div>
      </div>
    </div>`;
  }

  function bindSlots(el, r) {
    $$('.slot', el).forEach((li) => {
      const name = li.dataset.slot;
      const s = r.slots.find((x) => x.name === name);
      const rerender = () => { li.outerHTML = slotRow(s); bindSlots(el, r); renderSide(); };
      const sw = () => (S.studio.swaps || []).find((x) => x.slot === name);
      $('[data-toggle]', li).onclick = () => { S.openSlot = S.openSlot === name ? null : name; rerender(); };
      const take = async (file) => {
        if (!file) return;
        const ext = (file.name.split('.').pop() || '').toLowerCase();
        const isModel = MODEL_EXT.includes(ext);
        try {
          const up = await uploadFile(file, 'furniture');
          const keys = S.status.keys || {};
          const old = sw() || {};
          const entry = Object.assign({ turn: 0, scale: 1, colors: 'match', provider: 'auto' }, old, {
            slot: name, label: s.label, file: up.path, name: file.name, kind: isModel ? 'model' : 'photo',
            method: isModel ? '' : (old.method || ((keys.meshy?.set || keys.fal?.set) ? 'ai' : 'blocky')),
          });
          S.studio.swaps = (S.studio.swaps || []).filter((x) => x.slot !== name).concat([entry]);
          S.openSlot = name;
          changed(); rerender();
          toast(`${s.label}: ${isModel ? '3D model' : 'photo'} added. It goes into the room when you build.`, 'ok');
        } catch (e) { toast(e.message, 'error'); }
      };
      const drop = $('.slot-drop', li);
      const fileIn = $('input[type=file]', li);
      if (drop) {
        drop.onclick = () => fileIn.click();
        drop.onkeydown = (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); fileIn.click(); } };
        dropTarget(drop, (fs) => take(fs[0]));
      }
      if (fileIn) fileIn.onchange = () => take(fileIn.files[0]);
      const rep = $('[data-replace]', li);
      if (rep) { rep.onclick = () => fileIn.click(); dropTarget($('.swap-preview', li), (fs) => take(fs[0])); }
      const cur = sw();
      if (!cur) return;
      const set = (k, v, re = false) => { cur[k] = v; changed(); if (re) rerender(); else { const sm = $('.slot-text small', li); if (sm) sm.textContent = swapSummary(cur); } };
      $$('input[type=radio]', li).forEach((rb) => rb.onchange = () => {
        const keys = S.status.keys || {};
        if (rb.value === 'ai' && !(keys.meshy?.set || keys.fal?.set || keys.hf?.set) && (cur.provider || 'auto') === 'auto') toast('Add a Meshy or fal key in Settings, or pick “Demo model” or Hugging Face.', 'info', 6000);
        set('method', rb.value, true);
      });
      const prov = $('[data-provider]', li);
      if (prov) prov.onchange = () => set('provider', prov.value);
      $$('[data-turn]', li).forEach((b) => b.onclick = () => set('turn', +b.dataset.turn, true));
      const fine = $('[data-turnfine]', li);
      fine.oninput = () => { const v = (+fine.value + 360) % 360; cur.turn = v; $('[data-turnout]', li).textContent = `${v}°`; $('.slot-text small', li).textContent = swapSummary(cur); $$('[data-turn]', li).forEach((b) => { b.classList.toggle('on', +b.dataset.turn === v); }); changed(); };
      const sc = $('[data-scale]', li);
      sc.oninput = () => { cur.scale = +sc.value / 100; $('[data-scaleout]', li).textContent = `${sc.value}%`; $('.slot-text small', li).textContent = swapSummary(cur); changed(); };
      $$('[data-colors]', li).forEach((b) => b.onclick = () => set('colors', b.dataset.colors, true));
      $('[data-remove]', li).onclick = () => { S.studio.swaps = S.studio.swaps.filter((x) => x.slot !== name); S.openSlot = null; changed(); rerender(); };
    });
  }

  // ------------------------------------------------------------------ step 6: build
  function estimate(opts) {
    const tm = S.status.timings || {};
    const r = room();
    let s = tm.room || 20;
    (S.studio.swaps || []).forEach((sw) => { s += sw.kind === 'model' ? tm.furniture_model : sw.method === 'ai' ? tm.furniture_ai + tm.furniture_model : tm.furniture_photo; });
    const quick = opts.quality !== 'final';
    const n = quick ? 1 : (S.status.features?.exports ? opts.exports.length : 4);
    s += (quick ? tm.render_quick : tm.render_final) * Math.max(n, 1);
    if (opts.web) s += quick ? tm.web_quick : tm.web_final;
    void r;
    return s;
  }

  function viewBuild(el) {
    const b = S.status.blender;
    if (S.job && (S.job.state === 'running' || S.job.state === 'error' || S.job.state === 'cancelled')) return viewJob(el);
    if (b.state !== 'ok') {
      const prev = S.studio.last_build && S.outputs.index ? resultsHtml(S.studio.last_build) : '';
      el.innerHTML = header('Step 6 of 6', 'Build & publish', '') + blenderCard(b) + prev + navButtons('furnish', '');
      bindBlenderCard(el);
      if (prev) bindResults(el);
      return;
    }
    const opts = S.studio.build;
    const feats = S.status.features || {};
    const quick = opts.quality !== 'final';
    const lb = S.studio.last_build;
    const pre = preflight();
    const exportsHtml = Object.entries(S.exportsInfo).map(([id, x]) => {
      const supported = feats.exports || ['hero', 'og', 'instagram', 'banner'].includes(id);
      const on = id === 'hero' || (!quick && supported && (opts.exports || []).includes(id));
      const disabled = id === 'hero' || quick || !supported;
      return `<label class="exp ${disabled ? 'dis' : ''} ${on ? 'on' : ''}"><input type="checkbox" data-exp="${id}" ${on ? 'checked' : ''} ${disabled ? 'disabled' : ''}>
        <span class="exp-box" style="aspect-ratio:${x.size.replace(/\s/g, '').replace('×', '/')}"></span>
        <span class="exp-text"><strong>${esc(x.label)}</strong><small>${esc(x.size)}</small><small class="use">${!supported ? '<span class="soon">Next kit update</span>' : esc(x.use)}</small></span></label>`;
    }).join('');
    el.innerHTML = header('Step 6 of 6', 'Build & publish', 'RoomKit opens Blender in the background, puts you in the room and takes the pictures. You can keep working while it runs.') + `
      ${lb ? resultsHtml(lb) : ''}
      <section class="card build-card" id="build-card">
        <h2 class="card-title">${icon('sparkles')}${lb ? 'Build again' : 'Build settings'}</h2>
        <div class="quality" role="radiogroup" aria-label="Quality">
          <label class="q-card ${quick ? 'on' : ''}"><input type="radio" name="q" value="quick" ${quick ? 'checked' : ''}>
            <span class="q-title">${icon('play')}Quick preview</span><span class="q-time">${icon('clock', 'sm')}about ${esc(fmtDur(estimate(Object.assign({}, opts, { quality: 'quick' }))))}</span>
            <span class="q-desc">The main picture only, with softer lighting. Great for checking everything.</span></label>
          <label class="q-card ${!quick ? 'on' : ''}"><input type="radio" name="q" value="final" ${!quick ? 'checked' : ''}>
            <span class="q-title">${icon('star')}Final quality</span><span class="q-time">${icon('clock', 'sm')}about ${esc(fmtDur(estimate(Object.assign({}, opts, { quality: 'final' }))))}</span>
            <span class="q-desc">Every picture size you pick below, sharp and ready to share.</span></label>
        </div>
        <label class="switch big"><input type="checkbox" id="web" ${opts.web ? 'checked' : ''}><span class="track"></span>
          <span><strong>Include the 3D website</strong><small>Visitors can turn, zoom and click your room in the browser. Adds a few minutes.</small></span></label>
        <h3 class="sub">Picture sizes ${quick ? '<span class="muted small">(Quick preview makes the main picture only)</span>' : ''}</h3>
        <div class="exports">${exportsHtml}</div>
        <div class="preflight">${pre.map((x) => `<p class="${x.level}">${icon(x.level === 'ok' ? 'check' : x.level === 'error' ? 'alert' : 'info', 'sm')}${esc(x.msg)}${x.step ? ` <button class="link-btn" data-go="${x.step}">Fix</button>` : ''}</p>`).join('')}</div>
        <div class="build-go">
          <button class="btn primary xl" id="go" ${pre.some((x) => x.level === 'error') ? 'disabled' : ''}>${icon('sparkles')}${lb ? 'Build again' : 'Build my portfolio'}</button>
          <span class="muted">About ${esc(fmtDur(estimate(opts)))} on this computer</span>
        </div>
      </section>
      ${navButtons('furnish', '')}`;
    $$('input[name=q]', el).forEach((r) => r.onchange = () => { opts.quality = r.value; changed(); viewBuild(el); bindNav(el); });
    $('#web', el).onchange = (e) => { opts.web = e.target.checked; changed(); viewBuild(el); bindNav(el); };
    $$('[data-exp]', el).forEach((c) => c.onchange = () => {
      const set = new Set(opts.exports || []); c.checked ? set.add(c.dataset.exp) : set.delete(c.dataset.exp);
      opts.exports = Object.keys(S.exportsInfo).filter((k) => set.has(k) || k === 'hero');
      S.studio.touched.exports = true; changed(); c.closest('.exp').classList.toggle('on', c.checked);
    });
    $('#go', el).onclick = startBuild;
    bindResults(el);
  }

  function preflight() {
    const out = [];
    const p = S.profile;
    const nc = nameCheck();
    if (nc.level === 'error') out.push({ level: 'error', msg: nc.msg, step: 'profile' });
    else if (nc.level === 'warn') out.push({ level: 'warn', msg: 'Your name will be made a little smaller to fit the sign.', step: 'profile' });
    if (!room()) out.push({ level: 'error', msg: 'Choose a room first.', step: 'room' });
    const pics = (p.projects || []).filter((x) => x.image).length;
    if (!pics) out.push({ level: 'warn', msg: 'No project pictures yet - the room will show its own sample pictures.', step: 'projects' });
    if (!Object.keys(p.links || {}).length) out.push({ level: 'warn', msg: 'No links yet, so visitors can’t reach you.', step: 'profile' });
    const bad = Object.entries(p.links || {}).filter(([k, v]) => validateLink(k, v).level === 'error');
    if (bad.length) out.push({ level: 'warn', msg: `Check your ${bad.map(([k]) => (S.linkTypes[k] || {}).label || k).join(', ')} link.`, step: 'profile' });
    const ai = (S.studio.swaps || []).filter((s) => s.kind !== 'model' && s.method === 'ai');
    if (ai.length) out.push({ level: 'info', msg: `${ai.length} AI 3D model${ai.length > 1 ? 's' : ''} will be made. Paid services charge per model; it’s reused next time.` });
    if (!out.length) out.push({ level: 'ok', msg: 'Everything looks good.' });
    return out;
  }

  function blenderCard(b) {
    const os = (S.status.platform || '').toLowerCase();
    const where = os === 'darwin' ? 'Drag Blender into your Applications folder, then come back here.' : os === 'windows' ? 'Run the installer with the default options, then come back here.' : 'Install it from blender.org, Steam, Snap or your package manager, then come back here.';
    const title = b.state === 'checking' ? 'Looking for Blender…' : b.state === 'too_old' ? 'Your Blender is too old' : 'One more thing: install Blender (free)';
    return `<section class="card blender-card" id="blender-card">
      <div class="bc-icon">${icon(b.state === 'checking' ? 'refresh' : 'download', b.state === 'checking' ? 'spin' : '')}</div>
      <h2>${esc(title)}</h2>
      ${b.state === 'checking' ? '<p>This only takes a moment.</p>' : `
      <p>RoomKit uses Blender, the free 3D app, behind the scenes to take your pictures. You never need to open it.${b.state === 'too_old' ? ` We found Blender ${esc(b.too_old.map((x) => x.version).join(', '))}, but RoomKit needs ${esc(b.min)} or newer.` : ''}</p>
      <ol class="install"><li>Download <b>Blender ${esc(b.min)} LTS</b> or newer (about 300 MB).</li><li>${esc(where)}</li><li>Press <b>Check again</b>.</li></ol>
      <div class="row wrap"><a class="btn primary" href="${esc(b.lts)}" target="_blank" rel="noopener">${icon('download')}Download Blender ${esc(b.min)} LTS</a>
        <a class="btn ghost" href="${esc(b.download)}" target="_blank" rel="noopener">${icon('external')}Latest Blender</a>
        <button class="btn soft" id="bl-recheck">${icon('refresh')}Check again</button></div>
      <details class="manual"><summary>Blender is installed somewhere else?</summary>
        <div class="row"><input id="bl-path" placeholder="${os === 'windows' ? 'C:\\Program Files\\Blender Foundation\\Blender 4.2\\blender.exe' : os === 'darwin' ? '/Applications/Blender.app' : '/home/you/blender-4.2/blender'}" aria-label="Blender location"><button class="btn soft" id="bl-set">Use this</button></div></details>`}
    </section>`;
  }
  function bindBlenderCard(root) {
    const re = $('#bl-recheck', root);
    if (re) re.onclick = async () => { re.disabled = true; try { S.status.blender = await api('blender', { method: 'POST', body: {} }); S.status = await api('status'); renderTop(); renderMain(); if (S.status.blender.state !== 'ok') toast('Still no Blender 4.2+. Install it, then press Check again.', 'info'); else toast('Blender found!', 'ok'); } catch (e) { toast(e.message, 'error'); re.disabled = false; } };
    const set = $('#bl-set', root);
    if (set) set.onclick = async () => { try { S.status.blender = await api('blender', { method: 'POST', body: { path: $('#bl-path').value } }); S.status = await api('status'); renderTop(); renderMain(); toast('Blender found!', 'ok'); } catch (e) { toast(e.message, 'error'); } };
  }

  async function startBuild() {
    await save();
    try {
      primeChime();
      const opts = S.studio.build;
      S.job = await api(`projects/${enc(S.pid)}/build`, { method: 'POST', body: { quality: opts.quality, web: opts.web, exports: opts.exports } });
      S.jobSince = 0; S.logLines = [];
      renderMain();
      pollJob();
    } catch (e) { toast(e.message, 'error'); }
  }

  async function pollJob() {
    if (!S.job) return;
    try {
      const snap = await api(`jobs/${S.job.id}?since=${S.jobSince}`);
      S.logLines.push(...snap.lines);
      if (S.logLines.length > 6000) S.logLines.splice(0, S.logLines.length - 6000);
      S.jobSince = snap.next;
      S.job = snap;
      if (S.step === 'build') updateJobView();
      const sb = $('#sum-build');
      if (sb && snap.state === 'running') sb.innerHTML = `<span class="spinner light"></span>Building… ${Math.round(snap.progress * 100)}%`;
      if (snap.state === 'running') return setTimeout(pollJob, 900);
      document.title = 'RoomKit Studio';
      if (snap.state === 'done') {
        chime();
        const d = await api(`projects/${enc(S.pid)}`);
        S.outputs = d.outputs; S.studio.last_build = d.studio.last_build;
        S.job = null;
        if (S.step === 'build') renderMain();
        renderSide();
        toast('Your portfolio is ready!', 'ok', 6000);
        notify('Your portfolio is ready!');
      } else {
        if (S.step === 'build') renderMain();
        renderSide();                                              // the side button stops saying "Building…"
      }
    } catch (e) { setTimeout(pollJob, 2500); }
  }

  function viewJob(el) {
    const j = S.job;
    if (j.state === 'error' || j.state === 'cancelled') {
      const err = j.error || { title: 'Build cancelled', message: 'Nothing was changed. Your previous results are still there.', hint: '' };
      el.innerHTML = header('Step 6 of 6', 'Build & publish', '') + `
        <section class="card job-card ${j.state}">
          <div class="err-head">${icon(j.state === 'error' ? 'alert' : 'info')}<div><h2>${esc(err.title)}</h2><p>${esc(err.message)}</p>${err.hint ? `<p class="hint">${esc(err.hint)}</p>` : ''}</div></div>
          ${jobSteps(j)}
          <div class="row wrap"><button class="btn primary" id="retry">${icon('refresh')}Try again</button><button class="btn ghost" id="back-settings">${icon('left')}Back to build settings</button><button class="btn ghost" id="toggle-log" aria-expanded="${S.showLog}">${icon('info')}${S.showLog ? 'Hide details' : 'Details'}</button></div>
          <pre class="log" id="log" ${S.showLog ? '' : 'hidden'}>${esc(S.logLines.join('\n'))}</pre>
        </section>`;
      $('#retry').onclick = () => { S.job = null; startBuild(); };
      $('#back-settings').onclick = () => { S.job = null; renderMain(); };
      bindLogToggle();
      return;
    }
    el.innerHTML = header('Step 6 of 6', 'Building your portfolio', 'You can keep editing other steps while this runs. We’ll play a little sound when it’s done.') + `
      <section class="card job-card" aria-busy="true">
        <div class="job-top"><div><p class="big-pct" id="pct">0%</p><p class="muted" id="eta">Starting Blender…</p></div>
          <button class="btn ghost" id="cancel">${icon('stop')}Cancel</button></div>
        <div class="bar" role="progressbar" aria-label="Build progress" aria-valuemin="0" aria-valuemax="100" id="bar"><span id="fill"></span></div>
        <p class="job-detail" id="detail" aria-live="polite"></p>
        <div id="job-steps">${jobSteps(j)}</div>
        <button class="link-btn" id="toggle-log" aria-expanded="${S.showLog}">${icon('info', 'sm')}${S.showLog ? 'Hide details' : 'Show details'}</button>
        <pre class="log" id="log" ${S.showLog ? '' : 'hidden'}></pre>
      </section>`;
    $('#cancel').onclick = async () => {
      if (!(await confirmModal('Cancel this build?', 'Blender will stop. Your previous results stay as they are.', 'Cancel build', 'Keep building'))) return;
      api(`jobs/${j.id}/cancel`, { method: 'POST' }).catch((e) => toast(e.message, 'error'));
    };
    bindLogToggle();
    updateJobView();
  }

  function bindLogToggle() {
    const t = $('#toggle-log');
    if (!t) return;
    t.onclick = () => {
      S.showLog = !S.showLog;
      const log = $('#log'); log.hidden = !S.showLog;
      if (S.showLog) { log.textContent = S.logLines.join('\n'); log.scrollTop = log.scrollHeight; }
      t.setAttribute('aria-expanded', S.showLog);
      t.innerHTML = `${icon('info', 'sm')}${S.showLog ? 'Hide details' : 'Show details'}`;
    };
  }

  function jobSteps(j) {
    return `<ol class="job-steps">${j.steps.map((s) => `<li class="${s.status}">
      <span class="js-icon">${s.status === 'done' ? icon('check') : s.status === 'running' ? '<span class="spinner"></span>' : s.status === 'failed' ? icon('x') : s.status === 'skipped' ? icon('right') : '<span class="dotp"></span>'}</span>
      <span class="js-label">${esc(s.label)}</span><span class="js-time">${s.took != null ? esc(fmtDur(s.took)) : s.status === 'pending' ? '~' + esc(fmtDur(s.est)) : ''}</span></li>`).join('')}</ol>`;
  }

  function updateJobView() {
    const j = S.job;
    if (!j || j.state !== 'running') return;
    const pct = Math.round(j.progress * 100);
    const fill = $('#fill');
    if (!fill) return;
    fill.style.width = pct + '%';
    $('#bar').setAttribute('aria-valuenow', pct);
    $('#pct').textContent = pct + '%';
    $('#eta').textContent = j.eta > 0 ? `About ${fmtDur(j.eta)} left · ${fmtDur(j.elapsed)} so far` : 'Almost there…';
    const cur = j.steps[j.current];
    $('#detail').textContent = j.detail || (cur ? cur.label + '…' : '');
    $('#job-steps').innerHTML = jobSteps(j);
    document.title = `${pct}% · Building · RoomKit Studio`;
    const log = $('#log');
    if (log && S.showLog) { const atEnd = log.scrollTop + log.clientHeight >= log.scrollHeight - 30; log.textContent = S.logLines.join('\n'); if (atEnd) log.scrollTop = log.scrollHeight; }
  }

  function resultsHtml(lb) {
    const o = S.outputs;
    const v = (k) => (o[k] ? `?v=${o[k].mtime}` : '');
    const pics = Object.keys(S.exportsInfo).filter((k) => o[k]);
    const has3d = !!o.room3d;
    const zip = `/api/projects/${enc(S.pid)}/zip?token=${enc(TOKEN)}`;
    return `<section class="card results" id="results">
      <div class="res-head"><div><p class="kicker ok">${icon('check', 'sm')}Ready · ${esc(ago(lb.when))} · ${lb.quality === 'final' ? 'Final quality' : 'Quick preview'} · ${esc(fmtDur(lb.seconds))}</p><h2>Your portfolio is ready</h2></div></div>
      ${o.hero ? `<a class="res-hero" href="${esc(projectUrl('output/hero.png') + v('hero'))}" target="_blank" rel="noopener"><img src="${esc(projectUrl('output/hero.png') + v('hero'))}" alt="Your room portfolio picture"></a>` : ''}
      <div class="res-actions">
        ${has3d ? `<a class="btn primary" href="${esc(projectUrl('output/room3d.html'))}" target="_blank" rel="noopener">${icon('cube')}Open 3D website</a>` : ''}
        ${o.index ? `<a class="btn ${has3d ? 'soft' : 'primary'}" href="${esc(projectUrl('output/index.html'))}" target="_blank" rel="noopener">${icon('globe')}Open 2D site</a>` : ''}
        <button class="btn soft" id="open-out">${icon('folder')}Open folder</button>
        <a class="btn soft" href="${esc(zip)}" download>${icon('download')}Download .zip</a>
      </div>
      ${(lb.warnings || []).length ? `<div class="warns">${lb.warnings.map((w) => `<p>${icon('info', 'sm')}${esc(w)}</p>`).join('')}</div>` : ''}
      ${pics.length > 1 ? `<h3 class="sub">Pictures</h3><div class="pics">${pics.map((k) => `<a class="pic" href="${esc(projectUrl('output/' + o[k].file) + v(k))}" download="${esc(o[k].file)}"><img src="${esc(projectUrl('output/' + o[k].file) + v(k))}" alt="" loading="lazy"><span><strong>${esc(S.exportsInfo[k].label)}</strong><small>${esc(S.exportsInfo[k].size)}</small></span>${icon('download', 'sm')}</a>`).join('')}</div>` : ''}
      ${publishGuide()}
    </section>`;
  }

  const GUIDES = {
    netlify: {
      label: 'Netlify Drop (easiest)',
      steps: [
        'Press “Open folder”. The output folder is your whole website.',
        'Go to app.netlify.com/drop in your browser.',
        'Drag the output folder onto the page and wait a few seconds.',
        'Create a free account to claim your site straight away - unclaimed sites are deleted after about an hour.',
        'In Site configuration, choose “Change site name” to get a nicer address like yourname.netlify.app.',
        'To update later: build again, open your site in Netlify, go to Deploys and drag the new output folder.',
      ],
      link: 'https://app.netlify.com/drop',
    },
    github: {
      label: 'GitHub Pages',
      steps: [
        'Create a free account at github.com.',
        'Make a new public repository called yourname.github.io (use your GitHub username).',
        'Click “uploading an existing file” and drag in everything inside the output folder (not the folder itself). Press “Commit changes”.',
        'Open Settings → Pages. Under “Build and deployment”, choose “Deploy from a branch”, pick main and / (root), then Save.',
        'After a minute or two your site is live at https://yourname.github.io.',
        'To update later: upload the new files again - they replace the old ones.',
      ],
      link: 'https://pages.github.com/',
    },
  };

  function publishGuide() {
    const tab = safeStorage('get', 'roomkit.guide') || 'netlify';
    const g = GUIDES[tab] || GUIDES.netlify;
    const done = JSON.parse(safeStorage('get', `roomkit.check.${S.pid}.${tab}`) || '[]');
    return `<section class="publish" id="publish">
      <div class="pub-head"><h3 class="sub">${icon('globe')}Publish free</h3>
        <div class="tabs" role="tablist">${Object.entries(GUIDES).map(([id, x]) => `<button role="tab" class="tab ${id === tab ? 'on' : ''}" aria-selected="${id === tab}" data-guide="${id}">${esc(x.label)}</button>`).join('')}</div></div>
      <ol class="checklist">${g.steps.map((s, i) => `<li><label><input type="checkbox" data-check="${i}" ${done.includes(i) ? 'checked' : ''}><span>${esc(s)}</span></label></li>`).join('')}</ol>
      <div class="row wrap"><a class="btn soft sm" href="${esc(g.link)}" target="_blank" rel="noopener">${icon('external', 'sm')}Open ${esc(g.label.split(' (')[0])}</a><button class="btn ghost sm" id="copy-guide">${icon('copy', 'sm')}Copy checklist</button></div>
      <p class="muted small">Want your own address like yourname.com? Buy a domain from any registrar, then follow your host’s “custom domain” guide - both hosts are free with your own domain.</p>
    </section>`;
  }

  function bindResults(root) {
    const oo = $('#open-out', root);
    if (oo) oo.onclick = () => api(`projects/${enc(S.pid)}/open`, { method: 'POST', body: { what: 'output' } }).catch((e) => toast(e.message, 'error'));
    $$('[data-guide]', root).forEach((b) => b.onclick = () => { safeStorage('set', 'roomkit.guide', b.dataset.guide); const pub = $('#publish'); pub.outerHTML = publishGuide(); bindResults(root); });
    const tab = safeStorage('get', 'roomkit.guide') || 'netlify';
    $$('[data-check]', root).forEach((c) => c.onchange = () => {
      const key = `roomkit.check.${S.pid}.${tab}`;
      const done = new Set(JSON.parse(safeStorage('get', key) || '[]'));
      c.checked ? done.add(+c.dataset.check) : done.delete(+c.dataset.check);
      safeStorage('set', key, JSON.stringify(Array.from(done)));
    });
    const cg = $('#copy-guide', root);
    if (cg) cg.onclick = async () => {
      const g = GUIDES[tab] || GUIDES.netlify;
      const text = `Publish my RoomKit portfolio (${g.label})\n` + g.steps.map((s) => `[ ] ${s}`).join('\n') + `\n\nWebsite folder: ${S.folder}/output`;
      try { await navigator.clipboard.writeText(text); toast('Checklist copied.', 'ok'); }
      catch (e) { const ta = document.createElement('textarea'); ta.value = text; document.body.appendChild(ta); ta.select(); document.execCommand('copy'); ta.remove(); toast('Checklist copied.', 'ok'); }
    };
  }

  // ------------------------------------------------------------------ sound + notification when done
  let audio = null;
  function primeChime() { try { audio = audio || new (window.AudioContext || window.webkitAudioContext)(); } catch (e) { audio = null; } }
  function chime() {
    if (!audio) return;
    try {
      const now = audio.currentTime;
      [659.25, 880, 1174.66].forEach((f, i) => {
        const o = audio.createOscillator(), g = audio.createGain();
        o.type = 'sine'; o.frequency.value = f;
        g.gain.setValueAtTime(0.0001, now + i * 0.13);
        g.gain.exponentialRampToValueAtTime(0.12, now + i * 0.13 + 0.02);
        g.gain.exponentialRampToValueAtTime(0.0001, now + i * 0.13 + 0.5);
        o.connect(g).connect(audio.destination); o.start(now + i * 0.13); o.stop(now + i * 0.13 + 0.55);
      });
    } catch (e) { /* no sound is fine */ }
  }
  function notify(msg) {
    if (document.hasFocus() || !('Notification' in window)) return;
    if (Notification.permission === 'granted') new Notification('RoomKit Studio', { body: msg });
  }

  // ------------------------------------------------------------------ modals
  function modal(html, onMount) {
    const root = $('#modal-root');
    const prev = document.activeElement;
    root.innerHTML = `<div class="backdrop"><div class="modal" role="dialog" aria-modal="true" aria-labelledby="modal-title">${html}</div></div>`;
    const close = () => { root.innerHTML = ''; document.removeEventListener('keydown', onKey); if (prev && prev.focus) prev.focus(); };
    const onKey = (e) => {
      if (e.key === 'Escape') close();
      if (e.key === 'Tab') {
        const f = $$('button, input, select, textarea, a[href]', root).filter((x) => !x.disabled);
        if (!f.length) return;
        if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
        else if (!e.shiftKey && document.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
      }
    };
    document.addEventListener('keydown', onKey);
    $('.backdrop', root).addEventListener('mousedown', (e) => { if (e.target.classList.contains('backdrop')) close(); });
    onMount($('.modal', root), close);
    const first = $('[autofocus]', root) || $('input, button', root);
    if (first) first.focus();
    return close;
  }
  function confirmModal(title, text, yes = 'OK', no = 'Cancel') {
    return new Promise((resolve) => {
      modal(`<h2 id="modal-title">${esc(title)}</h2><p>${esc(text)}</p><div class="modal-actions"><button class="btn ghost" data-no>${esc(no)}</button><button class="btn primary" data-yes autofocus>${esc(yes)}</button></div>`, (m, close) => {
        $('[data-no]', m).onclick = () => { close(); resolve(false); };
        $('[data-yes]', m).onclick = () => { close(); resolve(true); };
      });
    });
  }
  function promptModal(title, label, value = '') {
    return new Promise((resolve) => {
      modal(`<h2 id="modal-title">${esc(title)}</h2><form><label class="flabel" for="pm-in">${esc(label)}</label><input id="pm-in" value="${esc(value)}" maxlength="60" autofocus required>
        <div class="modal-actions"><button type="button" class="btn ghost" data-no>Cancel</button><button class="btn primary" type="submit">Create</button></div></form>`, (m, close) => {
        $('[data-no]', m).onclick = () => { close(); resolve(''); };
        $('form', m).onsubmit = (e) => { e.preventDefault(); const v = $('#pm-in', m).value.trim(); close(); resolve(v); };
        setTimeout(() => $('#pm-in', m).select(), 0);
      });
    });
  }

  function openSettings(section = '') {
    const draw = (m, close) => {
      const k = S.status.keys || {};
      const b = S.status.blender;
      const svc = [
        ['meshy', 'Meshy', 'Best quality. Needs a Meshy Pro plan for API keys.', 'https://www.meshy.ai/api', 'msy_…'],
        ['fal', 'fal.ai', 'Pay per model (from about $0.02). No subscription.', 'https://fal.ai/dashboard/keys', 'Key ID:secret'],
        ['hf', 'Hugging Face', 'Free token for more daily free models (best effort).', 'https://huggingface.co/settings/tokens', 'hf_…'],
      ];
      m.innerHTML = `<div class="modal-head"><h2 id="modal-title">Settings</h2><button class="icon-btn" data-close aria-label="Close settings">${icon('x')}</button></div>
        <section class="set-sec" id="sec-keys"><h3>${icon('key')}AI 3D model keys</h3>
          <p class="muted small">Keys are saved only on this computer in <code>${esc(S.status.keys_file)}</code> (readable only by you). They are never put in your project or website.</p>
          ${svc.map(([id, name, desc, url, ph]) => `<div class="key-row">
            <div class="kr-text"><strong>${esc(name)}</strong><small>${esc(desc)} <a href="${esc(url)}" target="_blank" rel="noopener">Get a key</a></small></div>
            <div class="kr-ctl">${k[id] && k[id].set ? `<span class="status-pill on">${icon('check', 'sm')}Saved ${esc(k[id].hint)}</span>${k[id].from === 'keys.json' ? `<button class="btn ghost sm" data-rmkey="${id}">Remove</button>` : '<span class="muted small">from your environment</span>'}`
              : `<input type="password" autocomplete="off" spellcheck="false" placeholder="${esc(ph)}" data-key="${id}" aria-label="${esc(name)} key"><button class="btn soft sm" data-savekey="${id}">Save</button>`}</div></div>`).join('')}
        </section>
        <section class="set-sec" id="sec-blender"><h3>${icon('cube')}Blender</h3>
          ${b.state === 'ok' ? `<p>Using <b>Blender ${esc(b.version)}</b> <span class="muted small">(${esc(b.where)})</span><br><code class="path">${esc(b.path)}</code></p>` : `<p>${b.state === 'checking' ? 'Looking for Blender…' : 'Blender 4.2 or newer was not found.'} <a href="${esc(b.lts)}" target="_blank" rel="noopener">Download Blender</a></p>`}
          <div class="row"><input id="set-bl" placeholder="Choose another Blender (path to the app)" aria-label="Blender location"><button class="btn soft sm" id="set-bl-btn">Use</button><button class="btn ghost sm" id="set-bl-auto">${icon('refresh', 'sm')}Find automatically</button></div>
        </section>
        <section class="set-sec"><h3>${icon('folder')}Projects folder</h3><p><code class="path">${esc(S.status.workspace)}</code></p>
          <p class="muted small">Each project has its own folder with profile.json, images/, furniture/ and output/ (your website).</p></section>
        <section class="set-sec"><h3>${icon('refresh')}Rooms</h3><p class="muted small">${S.rooms.length} rooms found. New rooms in the templates folder appear automatically.</p>
          <button class="btn ghost sm" id="rescan">${icon('refresh', 'sm')}Check for new rooms</button></section>`;
      $('[data-close]', m).onclick = close;
      $$('[data-savekey]', m).forEach((btn) => btn.onclick = async () => {
        const id = btn.dataset.savekey; const val = $(`[data-key="${id}"]`, m).value.trim();
        if (!val) return toast('Paste your key first.', 'info');
        try { S.status.keys = await api('keys', { method: 'POST', body: { provider: id, key: val } }); toast('Key saved on this computer.', 'ok'); draw(m, close); if (S.step === 'furnish') renderMain(); } catch (e) { toast(e.message, 'error'); }
      });
      $$('[data-rmkey]', m).forEach((btn) => btn.onclick = async () => {
        try { S.status.keys = await api('keys', { method: 'POST', body: { provider: btn.dataset.rmkey, key: '' } }); draw(m, close); if (S.step === 'furnish') renderMain(); } catch (e) { toast(e.message, 'error'); }
      });
      $('#set-bl-btn', m).onclick = async () => { try { S.status.blender = await api('blender', { method: 'POST', body: { path: $('#set-bl', m).value } }); S.status = await api('status'); renderTop(); draw(m, close); toast('Blender updated.', 'ok'); } catch (e) { toast(e.message, 'error'); } };
      $('#set-bl-auto', m).onclick = async () => { try { S.status.blender = await api('blender', { method: 'POST', body: { reset: true } }); S.status = await api('status'); renderTop(); draw(m, close); } catch (e) { toast(e.message, 'error'); } };
      $('#rescan', m).onclick = async () => { await api('rooms/refresh', { method: 'POST' }); S.roomsScanning = true; pollRooms(); toast('Checking the templates folder for rooms…', 'info'); };
      if (section) { const sec = $(`#sec-${section}`, m); if (sec) { sec.classList.add('flash'); sec.scrollIntoView({ block: 'center' }); } }
    };
    modal('', (m, close) => { m.classList.add('wide'); draw(m, close); });
  }

  // ------------------------------------------------------------------ go
  window.addEventListener('beforeunload', (e) => { if (S.saveTimer && $('#save-state')?.dataset.state === 'pending') { save(); e.preventDefault(); } });
  boot();
})();
