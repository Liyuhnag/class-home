(function () {
  const current = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('[data-nav]').forEach((link) => {
    if (link.getAttribute('href') === current || link.getAttribute('href') === './' + current) {
      link.classList.add('is-active');
    }
  });

  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.setAttribute('aria-live', 'polite');
  document.body.appendChild(toast);

  const showToast = (text) => {
    toast.textContent = text;
    toast.classList.add('show');
    window.clearTimeout(showToast._timer);
    showToast._timer = window.setTimeout(() => toast.classList.remove('show'), 1800);
  };

  document.querySelectorAll('a[download]').forEach((link) => {
    link.addEventListener('click', () => {
      const name = link.getAttribute('download') || '文件';
      showToast('开始下载：' + name);
    });
  });

  document.querySelectorAll('[data-back]').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      if (history.length > 1) history.back();
      else window.location.href = '../index.html';
    });
  });

  const treeGroups = Array.from(document.querySelectorAll('.tree-group'));
  const setTreeOpen = (open) => treeGroups.forEach((group) => {
    group.open = open;
  });

  document.querySelectorAll('[data-tree-toggle]').forEach((btn) => {
    btn.addEventListener('click', () => {
      const action = btn.getAttribute('data-tree-toggle');
      if (action === 'expand') setTreeOpen(true);
      if (action === 'collapse') setTreeOpen(false);
    });
  });

  // 代码块一键复制
  document.querySelectorAll('.code-block').forEach((block) => {
    const btn = document.createElement('button');
    btn.className = 'code-copy-btn';
    btn.type = 'button';
    btn.textContent = '复制';
    block.appendChild(btn);
    btn.addEventListener('click', () => {
      const code = block.querySelector('code');
      const text = code ? code.textContent : block.textContent;
      navigator.clipboard.writeText(text).then(() => {
        btn.textContent = '已复制';
        btn.classList.add('copied');
        setTimeout(() => {
          btn.textContent = '复制';
          btn.classList.remove('copied');
        }, 1500);
      });
    });
  });
})();

