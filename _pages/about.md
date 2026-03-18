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

Hi 👋! I’m **Jingming Liang**, and you can also call me **Brighton**. I am from Dalian, China, and currently a **junior CS undergraduate** at the [**School of Computer Science**](https://cc.nankai.edu.cn/), [**Nankai University**](https://www.nankai.edu.cn/) <img src="{{ '/images/nankai-emblem.png' | relative_url }}" alt="Nankai University emblem" style="height: 1.1em; width: 1.1em; vertical-align: -0.15em; margin-left: 0.2em;">, pursuing dual minors in [**Finance**](https://finance.nankai.edu.cn/2024/0510/c34622a542022/page.htm) and **Criminal Law**.

Beyond my interdisciplinary studies, my main focus is building **efficient ML systems** and **scalable AI infrastructure**. I am actively looking for research and engineering opportunities in **ML Systems**, **Distributed AI**, and **Hardware-Aware Optimization**. Feel free to reach out through the email and social links in the sidebar!

**Research Interests:**

<ul class="research-interests-list">
  <li><strong>Efficient ML Systems and AI Infrastructure</strong>: Scalable training, efficient inference, and systems optimization for foundation models.</li>
  <li><strong>Distributed Systems for Large-Scale AI</strong>: Runtime efficiency, resource management, and parallel execution for modern AI workloads.</li>
  <li><strong>Hardware-Aware Model Optimization</strong>: Profiling-driven optimization, memory/computation tradeoff analysis, and deployment-oriented system design.</li>
</ul>


# 🔥 News
<ul class="news-list">
  <li class="news-list__item">
    <div class="news-list__meta">
      <strong class="news-list__date">[Mar 2026]</strong>
      <span class="news-list__status">Preparing Submission</span>
    </div>
    <span class="news-list__title">Stop-the-Hijack: Training-Free Router Stabilization for Reliable Grounding in Multimodal MoE Models</span>
    <span class="news-list__body">I am currently developing a solo research project in AI infrastructure and ML systems that studies how system prompts can hijack cross-modal MoE routing. By designing a framework that bypasses DeepSpeed's C++ operators through exact pseudo-inverse perturbations, I analyze this routing instability and explore practical interventions for mitigating it. A submission is in preparation.</span>
  </li>
</ul>

# 📝 Projects and Research

## Projects

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">GPU Systems</div><img src="{{ '/images/projects/optimized/apsp-gpu-optimization.webp' | relative_url }}" alt="APSP GPU optimization project overview" width="100%" loading="lazy" decoding="async" fetchpriority="low"></div></div>
<div class='paper-box-text' markdown="1">

**GPU Optimization for All-Pairs Shortest Path** <em>(Individual Competitor; CCF-TCARCH 2025 National Champion)</em>

- Designed a **memory-aware 3-stage blocked Floyd–Warshall pipeline** to reduce bandwidth pressure in dense APSP computation, using shared memory to improve data locality.
- Optimized kernel execution through fusion, dual-stream scheduling, double buffering, and reduced synchronization overhead. Further compressed **host-to-device transfer cost from O(V²) to O(E)** via custom I/O and device-side graph reconstruction.
- Ranked 1st nationally as an individual competitor, achieving a **52% end-to-end speedup** on the official hidden datasets (11.50s → 5.42s) through profiling-driven optimization and systematic performance tuning.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Information Systems</div><img src="{{ '/images/projects/optimized/raceradar-overview.webp' | relative_url }}" alt="RaceRadar iOS app overview" width="100%" loading="lazy" decoding="async" fetchpriority="low"></div></div>
<div class='paper-box-text' markdown="1">

**RaceRadar: An End-to-End iOS System for Aggregating and Prioritizing Competition Opportunities** <em>(Independent systems engineering project; App Store release in preparation)</em>

- Built a **fault-tolerant, multi-source ingestion pipeline** that continuously crawls, cleans, deduplicates, and ranks competition announcements, publishing a unified JSON feed through scheduled GitHub Actions workflows.
- Developed a **native iOS app in Swift/Xcode** with card-based discovery, detailed opportunity pages, deadline-aware prioritization, source/category tagging, and shareable competition posters.
- Designed the system around real student workflows, translating automated data ingestion and ranking into a **deployable user-facing information system** for discovering higher-quality and time-sensitive opportunities.
</div>
</div>

## Research

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">LTSF</div><img src="{{ '/images/projects/sparsetsf-fft-updated.png' | relative_url }}" alt="SparseTSF-FFT framework overview" width="100%" loading="lazy" decoding="async" fetchpriority="low"></div></div>
<div class='paper-box-text' markdown="1">

**SparseTSF-FFT: A Frequency-Domain Framework for Time Series Forecasting**

- **Reimplemented and extended SparseTSF from PyTorch to MindSpore**, including custom API mappings and reconstruction of the training/evaluation pipeline for cross-framework deployment.
- Designed an **FFT-based learnable filtering module** to replace local sliding-window convolutions, aiming to better capture long-range periodic structure under a lightweight parameter budget.
- Conducted cross-framework profiling and forecasting evaluations, observing **improved long-horizon performance** (e.g., at 336 and 720 steps on ETTh1/ETTh2) relative to the baseline.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Diffusion Models</div><img src="{{ '/images/projects/optimized/k-lora-overview-v2.webp' | relative_url }}" alt="K-LoRA project overview" width="100%" loading="lazy" decoding="async" fetchpriority="low"></div></div>
<div class='paper-box-text' markdown="1">

**Research on Adaptive Weight Selection for Image Diffusion Models** <em>(National 3rd Prize in Challenge Cup, K-LoRA++)</em>

- Extended the **training-free object-style fusion framework** (**CVPR 2025 K-LoRA**) by mathematically formulating and evaluating **8 distinct stage-aware scaling schedules** across diffusion timesteps.
- Demonstrated through **first-order derivative analysis** and **cross-domain experiments** that a **constant-derivative linear schedule** optimally balances **content fidelity** and **style consistency**, effectively preventing **structural distortion** and **visual jitter** during the fusion process.
- Facilitated the **end-to-end development** of the project's **interactive demo** and drove its **practical deployment** for downstream **generative applications**.
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

</div>

<div class="service-board">
  <div class="service-board__intro">
    <p class="service-board__eyebrow">Teaching, Leadership, and Service</p>
  </div>

  <div class="service-board__group">
    <p class="service-board__label">Roles</p>
    <div class="service-list">
      <article class="service-item">
        <span class="service-item__date">Sep 2025 - Jan 2026</span>
        <div class="service-item__body">
          <p class="service-item__title">Teaching Assistant</p>
          <p class="service-item__meta">Computer Hardware Fundamentals</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">Sep 2025 - Jan 2026</span>
        <div class="service-item__body">
          <p class="service-item__title">Student Assistant</p>
          <p class="service-item__meta">Youth League Committee Office</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">Sep 2023 - Present</span>
        <div class="service-item__body">
          <p class="service-item__title">Class Monitor &amp; Youth League Branch Deputy Secretary</p>
          <p class="service-item__meta">School of Computer Science</p>
        </div>
      </article>
    </div>
  </div>

  <div class="service-board__group">
    <p class="service-board__label">Service Impact</p>
    <div class="service-stat-strip">
      <span class="service-chip"><strong>213.4h</strong> Volunteer Service</span>
      <span class="service-chip"><strong>153h</strong> Social Practice</span>
      <span class="service-chip"><strong>530h</strong> Peer Learning Support</span>
    </div>
  </div>

  <div class="service-board__group">
    <p class="service-board__label">Selected Honors</p>
    <div class="service-honor-grid">
      <article class="service-item">
        <span class="service-item__date">2024, 2025</span>
        <div class="service-item__body">
          <p class="service-item__title">Outstanding Student Cadre</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2025</span>
        <div class="service-item__body">
          <p class="service-item__title">Outstanding Team</p>
          <p class="service-item__meta">Nankai Xiong'an Summer Social Practice</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2025</span>
        <div class="service-item__body">
          <p class="service-item__title">Outstanding Individual</p>
          <p class="service-item__meta">Teachers and Students Together in Four Aspects Social Practice</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2025</span>
        <div class="service-item__body">
          <p class="service-item__title">Leader of the May Fourth Red Flag Youth League Group</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2025</span>
        <div class="service-item__body">
          <p class="service-item__title">Outstanding Class Youth League Branch</p>
        </div>
      </article>

      <article class="service-item">
        <span class="service-item__date">2023</span>
        <div class="service-item__body">
          <p class="service-item__title">Official Representative</p>
          <p class="service-item__meta">Nankai University Student Congress</p>
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
      <img src="{{ '/images/internships/optimized/hejun-logo.webp' | relative_url }}" alt="Hejun Consulting logo" class="internship-card__logo" loading="lazy" decoding="async" fetchpriority="low" />
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
      <img src="{{ '/images/internships/optimized/chinasoft-logo.webp' | relative_url }}" alt="ChinaSoft International logo" class="internship-card__logo" loading="lazy" decoding="async" fetchpriority="low" />
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
      <img src="{{ '/images/internships/optimized/gtja-logo.webp' | relative_url }}" alt="Guotai Junan Securities logo" class="internship-card__logo" loading="lazy" decoding="async" fetchpriority="low" />
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

<span class='anchor' id='technical-communication'></span>

# 📡 Technical Communication
<div class="news-board">
  <div class="news-board__header">
    <p class="news-board__eyebrow">Public Engagement</p>
    <p class="news-board__intro">Beyond research, I enjoy sharing structured learning materials on computer science and AI through public-facing educational content. This experience has helped me practice technical communication and think more carefully about how complex ideas can be made accessible to broader audiences.</p>
  </div>

  <div class="news-board__content">
    <article class="news-feature">
      <h4 class="news-feature__headline">CS and AI Educational Outreach</h4>
      <p class="news-feature__body">I create structured study notes, learning resources, and course-oriented materials for student audiences, and I am continuing to expand this work toward broader computer science and AI topics.</p>
      <div class="news-feature__stats">
        <span class="news-stat"><strong>5,500+</strong> followers</span>
        <span class="news-stat"><strong>2.4M+</strong> total views</span>
        <span class="news-stat"><strong>129k+</strong> likes and saves</span>
      </div>
      <p class="news-feature__foot">This work has helped me think more deliberately about clarity, structure, and accessibility when communicating technical ideas.</p>
    </article>

    <section class="news-gallery" aria-label="Snapshots of public-facing educational content">
      <div class="news-gallery__head">
        <span class="news-gallery__label">Visual Highlights</span>
        <p class="news-gallery__caption">Selected examples of educational content</p>
      </div>
      <div class="news-gallery__grid">
        <figure class="news-gallery__shot">
          <img class="news-gallery__image" src="{{ '/images/news/optimized/xiaohongshu-post-2.webp' | relative_url }}" alt="Xiaohongshu educational post screenshot 2" loading="lazy" decoding="async" fetchpriority="low">
        </figure>
        <figure class="news-gallery__shot">
          <img class="news-gallery__image" src="{{ '/images/news/optimized/xiaohongshu-post-3.webp' | relative_url }}" alt="Xiaohongshu educational post screenshot 3" loading="lazy" decoding="async" fetchpriority="low">
        </figure>
        <figure class="news-gallery__shot">
          <img class="news-gallery__image" src="{{ '/images/news/optimized/xiaohongshu-post-4.webp' | relative_url }}" alt="Xiaohongshu educational post screenshot 4" loading="lazy" decoding="async" fetchpriority="low">
        </figure>
        <figure class="news-gallery__shot">
          <img class="news-gallery__image" src="{{ '/images/news/optimized/xiaohongshu-post-7.webp' | relative_url }}" alt="Xiaohongshu educational post screenshot 7" loading="lazy" decoding="async" fetchpriority="low">
        </figure>
      </div>
    </section>

    <article class="news-feature">
      <h4 class="news-feature__headline">Beyond Research</h4>
      <p class="news-feature__body">Outside academic work, I enjoy music, endurance sports, and independent travel. I have formal training in violin and guitar and regularly participate in marathon running. These experiences have shaped my discipline, resilience, and curiosity.</p>
    </article>
  </div>
</div>
