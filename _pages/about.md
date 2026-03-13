---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<div style="text-align: center; margin: 0 0 1.5rem 0;">
  <img
    src="{{ '/images/hero.svg' | relative_url }}"
    alt="Personal belief hero image"
    style="display: inline-block; width: 100%; max-width: 960px; height: auto;"
    loading="eager"
    decoding="async"
  />
</div>

<span class='anchor' id='about-me'></span>

Hi 👋! I’m **Jingming Liang**, and you can also call me **Brighton**. I’m from **Dalian, Liaoning, China**, currently a **junior undergraduate student** majoring in **Computer Science and Technology** at the [**School of Computer Science**](https://cc.nankai.edu.cn/), [**Nankai University**](https://www.nankai.edu.cn/) <img src="{{ '/images/nankai-emblem.png' | relative_url }}" alt="Nankai University emblem" style="height: 1.1em; width: 1.1em; vertical-align: -0.15em; margin-left: 0.2em;">, and pursuing minors in [**Finance**](https://finance.nankai.edu.cn/2024/0510/c34622a542022/page.htm) and **Criminal Law**. Driven by curiosity, I like to step into real problems and keep exploring what I truly want to build and pursue. Feel free to reach out through the email and social links in the sidebar.

**Research Interests:**

<ul class="research-interests-list">
  <li>Parallel and distributed training for large language models and agentic systems</li>
  <li>AI for education</li>
  <li>Interdisciplinary research at the intersection of computing, finance, and law</li>
</ul>


# 🔥 News
<div class="news-board">
  <div class="news-board__header">
    <p class="news-board__eyebrow">Latest</p>
  </div>

  <div class="news-board__content">
    <article class="news-feature">
      <div class="news-feature__top">
        <h4 class="news-feature__headline">Educational content creator on Xiaohongshu</h4>
        <span class="news-feature__tag">Educational Outreach</span>
      </div>
      <p class="news-feature__body">I freely share study resources and notes to help tens of thousands of students navigate learning challenges. I am now preparing computer science course content to support more learners through AI for education.</p>
      <div class="news-feature__stats">
        <span class="news-stat"><strong>5,500+</strong> followers</span>
        <span class="news-stat"><strong>2.4M+</strong> total views</span>
        <span class="news-stat"><strong>129k+</strong> likes and saves</span>
      </div>
      <p class="news-feature__foot">I aim to reach more learners through public-interest knowledge sharing.</p>
    </article>

    <section class="news-gallery" aria-label="Snapshots of Xiaohongshu educational content">
      <div class="news-gallery__head">
        <span class="news-gallery__label">Visual Highlights</span>
        <p class="news-gallery__caption">Recent snapshots from my Xiaohongshu educational outreach</p>
      </div>
      <div class="news-gallery__grid">
        <figure class="news-gallery__shot">
          <img class="news-gallery__image" src="{{ '/images/news/xiaohongshu-post-1.jpg' | relative_url }}" alt="Xiaohongshu educational post screenshot 1">
        </figure>
        <figure class="news-gallery__shot">
          <img class="news-gallery__image" src="{{ '/images/news/xiaohongshu-post-2.jpg' | relative_url }}" alt="Xiaohongshu educational post screenshot 2">
        </figure>
        <figure class="news-gallery__shot">
          <img class="news-gallery__image" src="{{ '/images/news/xiaohongshu-post-3.jpg' | relative_url }}" alt="Xiaohongshu educational post screenshot 3">
        </figure>
        <figure class="news-gallery__shot">
          <img class="news-gallery__image" src="{{ '/images/news/xiaohongshu-post-4.jpg' | relative_url }}" alt="Xiaohongshu educational post screenshot 4">
        </figure>
        <figure class="news-gallery__shot">
          <img class="news-gallery__image" src="{{ '/images/news/xiaohongshu-post-5.jpg' | relative_url }}" alt="Xiaohongshu educational post screenshot 5">
        </figure>
        <figure class="news-gallery__shot">
          <img class="news-gallery__image" src="{{ '/images/news/xiaohongshu-post-6.jpg' | relative_url }}" alt="Xiaohongshu educational post screenshot 6">
        </figure>
        <figure class="news-gallery__shot">
          <img class="news-gallery__image" src="{{ '/images/news/xiaohongshu-post-7.jpg' | relative_url }}" alt="Xiaohongshu educational post screenshot 7">
        </figure>
        <figure class="news-gallery__shot">
          <img class="news-gallery__image" src="{{ '/images/news/xiaohongshu-post-8.jpg' | relative_url }}" alt="Xiaohongshu educational post screenshot 8">
        </figure>
      </div>
    </section>
  </div>
</div>

# 📝 Projects and Research

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Diffusion Models</div><img src='images/projects/k-lora-overview-v2.png' alt="K-LoRA project overview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Research on Personalized Image Diffusion Models with Adaptive Weight Selection**

- Extended the **CVPR 2025 K-LoRA** framework for training-free object-style fusion in diffusion models.
- Designed and analyzed **K-LoRA++ scale-factor schedules**, covering both linear and nonlinear variants.
- Ran cross-domain fusion and ablation experiments, showing that **linear schedules** provide the best balance of controllability, smooth transitions, and content fidelity.
- Supported the project’s **practical implementation and downstream deployment**.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">LTSF</div><img src='images/projects/sparsetsf-fft.png' alt="SparseTSF-FFT framework overview" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**SparseTSF-FFT: A Frequency-Domain Optimized Framework for Time Series Forecasting**

- Led the **PyTorch-to-MindSpore migration** of SparseTSF, rebuilding the training and evaluation pipeline, implementing missing operator equivalents, and open-sourcing the code.
- Proposed **SparseTSF-FFT**, an FFT-based learnable filtering framework for long-term time series forecasting that replaces local convolutions while preserving the model’s **sub-1k parameter budget**.
- Reproduced weight-pattern visualizations, compared runtime and MSE across frameworks, and achieved stronger long-horizon forecasting results on **ETTh1** and **ETTh2**.
</div>
</div>

# 🎖 Honors and Awards
<div class="award-board">
  <div class="award-board__intro">
    <p class="award-board__eyebrow">🏆 Competition Awards</p>
  </div>

  <section class="award-year-section">
    <div class="award-year-section__header">
      <h4 class="award-year-section__title">2025</h4>
      <p class="award-year-section__meta">12 awards</p>
    </div>
    <div class="award-grid">
      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.12</span>
          <span class="award-card__result">Second Place</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://forum.trae.cn/t/topic/213" target="_blank" rel="noopener noreferrer">TRAE on Campus Vibe Coding Workshop</a></h5>
        <div class="award-card__tags">
          <span class="award-card__tag award-card__tag--money">Prize ¥1,500</span>
        </div>
      </article>

      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.12</span>
          <span class="award-card__result">Bronze Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://news.nankai.edu.cn/zhxw/system/2025/12/08/030070061.shtml" target="_blank" rel="noopener noreferrer">3rd National College Student Career Planning Competition - Growth Track, University-level Competition</a></h5>
      </article>

      <article class="award-card award-card--featured">
        <span class="award-card__spotlight">Featured Award</span>
        <div class="award-card__top">
          <span class="award-card__date">2025.11</span>
          <span class="award-card__result">National Third Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://www.jiemian.com/article/13643188.html" target="_blank" rel="noopener noreferrer">National College Student Computer System Ability Competition</a></h5>
        <div class="award-card__tags">
          <span class="award-card__tag award-card__tag--money">Prize ¥10,000</span>
        </div>
      </article>

      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.11</span>
          <span class="award-card__result">Provincial First Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://www.cmathc.org.cn/mcm/news/362.html" target="_blank" rel="noopener noreferrer">China Undergraduate Mathematical Contest in Modeling (CUMCM)</a></h5>
      </article>

      <article class="award-card award-card--featured">
        <span class="award-card__spotlight">Featured Award</span>
        <div class="award-card__top">
          <span class="award-card__date">2025.10</span>
          <span class="award-card__result">National Third Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://news.nankai.edu.cn/ywsd/system/2025/11/10/030069539.shtml" target="_blank" rel="noopener noreferrer">19th Challenge Cup National College Student Extracurricular Academic and Technological Works Competition</a></h5>
      </article>

      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.10</span>
          <span class="award-card__result">Silver Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://mp.weixin.qq.com/s/bO7zPc8JcLDxAw58Q5PqqQ" target="_blank" rel="noopener noreferrer">Nankai University Mathematical Modeling Competition</a></h5>
      </article>

      <article class="award-card award-card--flagship">
        <span class="award-card__spotlight">Flagship Award</span>
        <div class="award-card__top">
          <span class="award-card__date">2025.09</span>
          <span class="award-card__result">National Champion</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://cc-backend.nankai.edu.cn/news/news-detail/20808" target="_blank" rel="noopener noreferrer">8th CCF-TCARCH Computer Architecture Challenge</a></h5>
        <div class="award-card__tags">
          <span class="award-card__tag award-card__tag--money">Prize ¥10,000</span>
        </div>
      </article>

      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.09</span>
          <span class="award-card__result">Special Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://mp.weixin.qq.com/s/npz3o1DdSBSMQ_omhiGmcw" target="_blank" rel="noopener noreferrer">Pioneer Cup Intelligent Computing Design Competition</a></h5>
        <div class="award-card__tags">
          <span class="award-card__tag award-card__tag--money">Prize ¥1,000</span>
        </div>
      </article>

      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.07</span>
          <span class="award-card__result">Special Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://2025.tiaozhanbei.net/d49/article/666/" target="_blank" rel="noopener noreferrer">18th Challenge Cup China Bank Tianjin Undergraduate Extracurricular Academic and Technological Works Competition</a></h5>
      </article>

      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.06</span>
          <span class="award-card__result">Outstanding Award</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://nktw.nankai.edu.cn/info/1013/1910.htm" target="_blank" rel="noopener noreferrer">President's Cup Innovation and Entrepreneurship Competition - Entrepreneurship Track</a></h5>
      </article>

      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.04</span>
          <span class="award-card__result">First Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://nktw.nankai.edu.cn/info/1013/1879.htm" target="_blank" rel="noopener noreferrer">President's Cup Innovation and Entrepreneurship Competition - Innovation Track</a></h5>
      </article>

      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.01</span>
          <span class="award-card__result">Honorable Mention, H Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://www.comap.com/contests/mcm-icm" target="_blank" rel="noopener noreferrer">Mathematical Contest in Modeling / Interdisciplinary Contest in Modeling (MCM/ICM)</a></h5>
      </article>
    </div>
  </section>

  <section class="award-year-section">
    <div class="award-year-section__header">
      <h4 class="award-year-section__title">2024</h4>
      <p class="award-year-section__meta">2 awards</p>
    </div>
    <div class="award-grid">
      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2024.11</span>
          <span class="award-card__result">Provincial Second Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://jw.tjut.edu.cn/info/1888/6440.htm" target="_blank" rel="noopener noreferrer">China Undergraduate Mathematical Contest in Modeling (CUMCM)</a></h5>
      </article>

      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2024.10</span>
          <span class="award-card__result">First Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://zhuanlan.zhihu.com/p/10010914554" target="_blank" rel="noopener noreferrer">3rd National College Student Data Analysis Popular Science Competition</a></h5>
      </article>
    </div>
  </section>

  <section class="award-year-section">
    <div class="award-year-section__header">
      <h4 class="award-year-section__title">2020</h4>
      <p class="award-year-section__meta">1 award</p>
    </div>
    <div class="award-grid">
      <article class="award-card">
        <div class="award-card__top">
          <span class="award-card__date">2020.06</span>
          <span class="award-card__result">Provincial First Prize</span>
        </div>
        <h5 class="award-card__name"><a class="award-card__link" href="https://www.zhyww.cn" target="_blank" rel="noopener noreferrer">22nd Yuwen Bao Cup National Middle School Student Themed Essay Campaign</a></h5>
      </article>
    </div>
  </section>
</div>

<div class="service-board">
  <div class="service-board__intro">
    <p class="service-board__eyebrow">🎖 Student Leadership and Service</p>
  </div>

  <div class="service-board__group">
    <p class="service-board__label">Positions</p>
    <div class="service-list">
      <article class="service-item">
        <span class="service-item__date">2025.09-2026.01</span>
        <div class="service-item__body">
          <p class="service-item__title">Teaching Assistant</p>
          <p class="service-item__meta">Computer Hardware Fundamentals</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2025.09-2026.01</span>
        <div class="service-item__body">
          <p class="service-item__title">Student Assistant</p>
          <p class="service-item__meta">Youth League Committee Office</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2023.09-Present</span>
        <div class="service-item__body">
          <p class="service-item__title">Class Monitor and Deputy Secretary of the Youth League Branch</p>
          <p class="service-item__meta">School of Computer Science</p>
        </div>
      </article>
    </div>
    <p class="service-inline-note"><strong>Campus Ambassador:</strong> EY, PwC, ByteDance, and Meituan</p>
  </div>

  <div class="service-board__group">
    <p class="service-board__label">Service Hours</p>
    <div class="service-stat-strip">
      <span class="service-chip"><strong>213.4h</strong> Volunteer Service</span>
      <span class="service-chip"><strong>153h</strong> Social Practice</span>
      <span class="service-chip"><strong>530h</strong> Ligong Zengneng Learning Support Platform</span>
    </div>
  </div>

  <div class="service-board__group">
    <p class="service-board__label">Honors</p>
    <div class="service-honor-grid">
      <article class="service-item">
        <span class="service-item__date">2025.11</span>
        <div class="service-item__body">
          <p class="service-item__title">Outstanding Student Cadre</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2025.11</span>
        <div class="service-item__body">
          <p class="service-item__title">Outstanding Individual</p>
          <p class="service-item__meta">Nankai "Teachers and Students Together in Four Aspects" Social Practice</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2025.11</span>
        <div class="service-item__body">
          <p class="service-item__title">Outstanding Team</p>
          <p class="service-item__meta">Nankai Xiong'an Summer Social Practice</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2025.06</span>
        <div class="service-item__body">
          <p class="service-item__title">Outstanding Class Youth League Branch</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2025.05</span>
        <div class="service-item__body">
          <p class="service-item__title">Leader of the May Fourth Red Flag Youth League Group</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2025.05</span>
        <div class="service-item__body">
          <p class="service-item__title">Official Advisor</p>
          <p class="service-item__meta">Nankai Student Affairs Committee</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2024.11</span>
        <div class="service-item__body">
          <p class="service-item__title">Outstanding Student Cadre</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2024.09</span>
        <div class="service-item__body">
          <p class="service-item__title">Outstanding Deputy Platoon Leader</p>
          <p class="service-item__meta">Nankai University Military Training</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2024.06</span>
        <div class="service-item__body">
          <p class="service-item__title">Outstanding Officer</p>
          <p class="service-item__meta">Nankai University CYL Organization Dept.</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2023.11</span>
        <div class="service-item__body">
          <p class="service-item__title">Participant</p>
          <p class="service-item__meta">Phase III "Zhuoyu Program"; representative speech at Zhou Enlai birthday commemoration</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2023.10</span>
        <div class="service-item__body">
          <p class="service-item__title">Official Representative</p>
          <p class="service-item__meta">Nankai University Student Congress</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2018.05</span>
        <div class="service-item__body">
          <p class="service-item__title">Dalian Merit Student</p>
        </div>
      </article>
    </div>
  </div>

</div>

# 🏅 Scholarships
<div class="award-board scholarship-board">
  <section class="award-year-section">
    <div class="award-year-section__header">
      <h4 class="award-year-section__title">2025</h4>
      <p class="award-year-section__meta">2 scholarships</p>
    </div>
    <div class="award-grid">
      <article class="award-card scholarship-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.11</span>
          <span class="award-card__result scholarship-card__amount">CNY 2,000</span>
        </div>
        <h5 class="award-card__name">Academic Progress Scholarship</h5>
        <p class="award-card__subtitle">Nankai University</p>
      </article>

      <article class="award-card scholarship-card">
        <div class="award-card__top">
          <span class="award-card__date">2025.11</span>
          <span class="award-card__result scholarship-card__amount">CNY 2,000</span>
        </div>
        <h5 class="award-card__name">Student Service Scholarship</h5>
        <p class="award-card__subtitle">Nankai University</p>
      </article>
    </div>
  </section>

  <section class="award-year-section">
    <div class="award-year-section__header">
      <h4 class="award-year-section__title">2024</h4>
      <p class="award-year-section__meta">2 scholarships</p>
    </div>
    <div class="award-grid">
      <article class="award-card scholarship-card">
        <div class="award-card__top">
          <span class="award-card__date">2024.11</span>
          <span class="award-card__result scholarship-card__amount">CNY 2,000</span>
        </div>
        <h5 class="award-card__name">Social Welfare Scholarship</h5>
        <p class="award-card__subtitle">Nankai University</p>
      </article>

      <article class="award-card scholarship-card">
        <div class="award-card__top">
          <span class="award-card__date">2024.11</span>
          <span class="award-card__result scholarship-card__amount">CNY 2,000</span>
        </div>
        <h5 class="award-card__name">Student Service Scholarship</h5>
        <p class="award-card__subtitle">Nankai University</p>
      </article>
    </div>
  </section>
</div>

<span class='anchor' id='arts-athletics'></span>

# 🎭 Arts and Athletics Achievements
<div class="arts-athletics-grid">
  <article class="achievement-card achievement-card--arts">
    <div class="achievement-card__header">
      <h3 class="achievement-card__title">Arts</h3>
      <span class="achievement-card__tag">Creative Track</span>
    </div>
    <ul class="achievement-card__list">
      <li class="achievement-card__item">
        <span class="achievement-card__year">2018</span>
        <div class="achievement-card__text">
          <strong>Classical Guitar Grade 10 Examination.</strong>
          I earned Classical Guitar Grade 10 with an <span class="achievement-award achievement-award--excellent">Excellent rating</span>, becoming <span class="achievement-award">the first student in Zhuanghe, Dalian</span> to do so, and was recognized by experts for my potential in <span class="achievement-award">classical guitar performance</span>.
        </div>
      </li>
      <li class="achievement-card__item">
        <span class="achievement-card__year">2018</span>
        <div class="achievement-card__text">
          <strong>4th Hai Zhi Xing Guitar Competition.</strong>
          I won <span class="achievement-award achievement-award--silver">Silver Prize</span> in Youth <span class="achievement-award">Folk Guitar</span> Group A and <span class="achievement-award achievement-award--silver">Silver Prize</span> in Children Classical Group, and was invited to perform on <span class="achievement-award">CCTV-15 Music Channel</span>.
        </div>
      </li>
      <li class="achievement-card__item">
        <span class="achievement-card__year">2015</span>
        <div class="achievement-card__text">
          <strong>National Arts Specialty Evaluation Certification.</strong>
          I passed Folk Guitar Grade 6 and received the <span class="achievement-award achievement-award--accent">Best</span> level.
        </div>
      </li>
      <li class="achievement-card__item">
        <span class="achievement-card__year">2014</span>
        <div class="achievement-card__text">
          <strong>China Conservatory of Music Violin Examination.</strong>
          I passed Violin <span class="achievement-award achievement-award--grade">Grade 10</span> and obtained the certificate.
        </div>
      </li>
      <li class="achievement-card__item">
        <span class="achievement-card__year">2011</span>
        <div class="achievement-card__text">
          <strong>"China Star" National Youth Outstanding Arts Talent Showcase.</strong>
          I won <span class="achievement-award achievement-award--gold">Gold Prize</span> in violin ensemble and <span class="achievement-award achievement-award--silver">Silver Prize</span> in violin solo performance.
        </div>
      </li>
    </ul>
  </article>

  <article class="achievement-card achievement-card--sports achievement-card--sports-profile">
    <div class="achievement-card__header">
      <h3 class="achievement-card__title">Athlete Profile</h3>
      <span class="achievement-card__tag">Endurance and Team Sports</span>
    </div>
    <div class="athlete-passion__intro">
      <p class="athlete-passion__lead">I am a passionate enthusiast of ball sports and marathon running.</p>
      <div class="athlete-passion__chips">
        <span class="athlete-passion__chip">Basketball</span>
        <span class="athlete-passion__chip">Football</span>
        <span class="athlete-passion__chip">Badminton</span>
        <span class="athlete-passion__chip">Table Tennis</span>
        <span class="athlete-passion__chip">Marathon</span>
        <span class="athlete-passion__chip">Volleyball</span>
      </div>
    </div>
    <section class="athlete-passion__results-section">
      <p class="athlete-passion__results-title">Selected Running Results</p>
      <ul class="athlete-passion__results">
        <li class="athlete-passion__result"><span class="athlete-passion__date">2024.04.27</span> Tianjin Jinnan Half Marathon <span class="athlete-passion__metric">1:45:13</span></li>
        <li class="athlete-passion__result"><span class="athlete-passion__date">2024.05.25</span> Nankai University Campus Marathon <span class="athlete-passion__metric">41:48, 10 km, 8th Place</span> (interviewed by Nankai University's official media)</li>
        <li class="athlete-passion__result"><span class="athlete-passion__date">2024.10.20</span> Tianjin Marathon (Full Marathon) <span class="athlete-passion__metric">3:58:40</span></li>
        <li class="athlete-passion__result"><span class="athlete-passion__date">2025.04.20</span> Tianjin Jinnan Half Marathon <span class="athlete-passion__metric">1:43:47</span></li>
        <li class="athlete-passion__result"><span class="athlete-passion__date">2025.05.17</span> Nankai University Campus Marathon <span class="athlete-passion__metric">44:44, 10 km</span></li>
      </ul>
      <div class="athlete-passion__gallery">
        <a class="athlete-passion__photo-link" href="{{ '/images/20260303-143716.png' | relative_url }}" target="_blank" rel="noopener noreferrer">
          <img src="{{ '/images/20260303-143716.png' | relative_url }}" alt="Running moment 1" class="athlete-passion__photo" loading="lazy" decoding="async" />
        </a>
        <a class="athlete-passion__photo-link" href="{{ '/images/20260303-143751.jpeg' | relative_url }}" target="_blank" rel="noopener noreferrer">
          <img src="{{ '/images/20260303-143751.jpeg' | relative_url }}" alt="Running moment 2" class="athlete-passion__photo" loading="lazy" decoding="async" />
        </a>
        <a class="athlete-passion__photo-link" href="{{ '/images/20260303144351.jpg' | relative_url }}" target="_blank" rel="noopener noreferrer">
          <img src="{{ '/images/20260303144351.jpg' | relative_url }}" alt="Running moment 3" class="athlete-passion__photo" loading="lazy" decoding="async" />
        </a>
      </div>
    </section>
  </article>
</div>

# 📖 Educations
<div class="education-card">
  <div class="education-card__header">
    <div class="education-card__main">
      <h3 class="education-card__school">Nankai University, School of Computer Science</h3>
      <p class="education-card__meta">Sep 2023 - Jun 2027 (Expected)</p>
      <div class="education-card__details">
        <p class="education-card__degree">B.Eng. Candidate in Computer Science and Technology</p>
        <p class="education-card__minor">Minors: Finance, Criminal Law.</p>
      </div>
    </div>
    <div class="education-card__side">
      <div class="education-card__tags">
        <span class="education-tag education-tag--strong">985 Project</span>
        <span class="education-tag education-tag--strong">211 Project</span>
        <span class="education-tag education-tag--soft">Double First-Class</span>
      </div>
      <img src="{{ '/images/nankai-emblem.png' | relative_url }}" alt="Nankai University emblem" class="education-card__emblem" loading="lazy" decoding="async" />
    </div>
  </div>
</div>

# 💼 Internships
<div class="internship-list">
  <article class="internship-card internship-card--featured internship-card--theme-hejun">
    <div class="internship-card__header">
      <img src="{{ '/images/internships/hejun-logo.png' | relative_url }}" alt="Hejun Consulting logo" class="internship-card__logo" loading="lazy" decoding="async" />
      <div class="internship-card__header-main">
        <h3 class="internship-card__company">Hejun Consulting</h3>
        <p class="internship-card__meta">Jul 2025 - Sep 2025</p>
      </div>
      <div class="internship-card__tags">
        <span class="internship-tag internship-tag--highlight">Top Domestic Consulting Firm</span>
      </div>
    </div>
    <ul class="internship-card__highlights">
      <li><strong>Served a leading Tianjin listed water utility</strong>, supporting strategic modules including the Fifteenth Five-Year Plan, technical pathways, and Jing-Jin-Ji collaboration initiatives.</li>
      <li><strong>Built evidence-ready research inputs</strong> by programmatically collecting and cleaning public disclosures (CNINFO, prospectuses, and official filings) for consulting workstreams.</li>
      <li><strong>Independently delivered a 30,000+ word insight report</strong> covering PEST, SWOT, value-chain mapping, peer benchmarking, and actionable improvement recommendations.</li>
    </ul>
  </article>

  <article class="internship-card internship-card--featured internship-card--theme-chinasoft">
    <div class="internship-card__header">
      <img src="{{ '/images/internships/chinasoft-logo.png' | relative_url }}" alt="ChinaSoft International logo" class="internship-card__logo" loading="lazy" decoding="async" />
      <div class="internship-card__header-main">
        <h3 class="internship-card__company">ChinaSoft International, LLM Team</h3>
        <p class="internship-card__meta">Jun 2025 - Jul 2025</p>
      </div>
      <div class="internship-card__tags">
        <span class="internship-tag internship-tag--highlight">Enterprise AI</span>
      </div>
    </div>
    <ul class="internship-card__highlights">
      <li><strong>Built enterprise-ready LLM workflows</strong> using DeepSeek-based applications and LangChain integration for practical business scenarios.</li>
      <li><strong>Engineered production-oriented AI services</strong> with PyTorch and FastAPI, including model tuning practices for vertical-domain performance.</li>
      <li><strong>Delivered a deployable intelligent assistant system</strong> built on chatbot frameworks (Maibot and Astrbot), with knowledge-base QA, persona settings, automated deployment, and dialogue analytics.</li>
    </ul>
  </article>

  <article class="internship-card internship-card--featured internship-card--theme-gtja">
    <div class="internship-card__header">
      <img src="{{ '/images/internships/gtja-logo.png' | relative_url }}" alt="Guotai Junan Securities logo" class="internship-card__logo" loading="lazy" decoding="async" />
      <div class="internship-card__header-main">
        <h3 class="internship-card__company">Guotai Junan Securities, Wealth Management</h3>
        <p class="internship-card__meta">Jun 2024 - Jul 2024</p>
      </div>
      <div class="internship-card__tags">
        <span class="internship-tag internship-tag--highlight">Top-Tier Securities Firm</span>
      </div>
    </div>
    <ul class="internship-card__highlights">
      <li><strong>Constructed IPS-based client planning workflows</strong> and applied the RRTTLLU constraint analysis framework for practical asset-allocation decisions.</li>
      <li><strong>Completed an end-to-end personal finance case</strong> covering quantitative profiling, cross-asset allocation modeling, and benchmark comparison against market indices.</li>
      <li><strong>Proposed dynamic rebalancing actions</strong> to improve return-risk balance while remaining aligned with long-term goals and client risk tolerance.</li>
    </ul>
  </article>
</div>
