import streamlit as st
from pathlib import Path

# Core site data (kept from original app)
services = {
    'seo': {
        'title': 'Search Engine Optimization (SEO)',
        'desc': '''We increase organic visibility through technical SEO, on-page optimization, keyword research, content strategy, link-building and local SEO. Our approach focuses on sustainable rankings, improved crawlability, faster page speed, schema implementation and content that converts users into customers.'''
    },
    'sem': {
        'title': 'Search Engine Marketing (SEM)',
        'desc': '''Paid search campaigns designed for intent-driven acquisition. We manage account structure, keyword bidding strategy, ad copy testing, conversion tracking and ROI-driven optimization across Google Ads and Microsoft Advertising.'''
    },
    'paid-advertising': {
        'title': 'Paid Advertising',
        'desc': '''Performance-focused paid advertising across search, social and programmatic channels. We build audience-first strategies, creative testing, conversion funnels, attribution and optimization to scale profitable acquisition.'''
    },
    'content-marketing': {
        'title': 'Content Marketing',
        'desc': '''Strategic content programs that attract, engage and retain audiences. We craft editorial roadmaps, pillar content, distribution plans, content repurposing and measurement to drive traffic and authority.'''
    },
    'website-services': {
        'title': 'Website Services',
        'desc': '''Design and development of high-performance websites with focus on UX, accessibility, speed and conversion. Includes CMS integration, e-commerce, responsive design and headless architectures where appropriate.'''
    },
    'branding-services': {
        'title': 'Branding Services',
        'desc': '''Positioning, identity systems, messaging and visual design that create memorable brands. We develop brand guidelines, visual assets, and campaign creative aligned to business goals.'''
    },
    'email-marketing': {
        'title': 'Email Marketing',
        'desc': '''Lifecycle email programs including acquisition flows, onboarding sequences, newsletters, promotional campaigns, segmentation and deliverability best practices to maximize engagement.'''
    },
    'marketing-automation': {
        'title': 'Marketing Automation',
        'desc': '''Automation workflows that trigger personalized messages across channels. We map customer journeys, implement automation platforms, and optimize for conversion and retention.'''
    },
    'analytics-and-tracking': {
        'title': 'Analytics & Tracking',
        'desc': '''Robust analytics setups: event tracking, GA/GA4 configuration, tag management, dashboards and measurement frameworks that turn data into action.'''
    },
    'online-reputation-management': {
        'title': 'Online Reputation Management',
        'desc': '''Protect and grow your brand reputation through review management, monitoring, response strategies, and proactive content to showcase positive customer experiences.'''
    }
}

testimonials = [
    {
        'title': 'Public Doctrine',
        'site': 'http://publicdoctrine.in/',
        'quote': 'High-quality website build with clean design and strong performance.'
    },
    {
        'title': 'Shreejee Foam',
        'site': 'http://shreejeefoam.in/',
        'quote': 'Responsive redesign and SEO-focused structure improved visibility.'
    },
    {
        'title': 'The BWCS',
        'site': 'http://thebwcs.com/',
        'quote': 'A modern, conversion-focused site delivered on time.'
    }
]


def render_css():
    # Inject a compact set of styles adapted from the original CSS to keep the bold/vibrant theme
    st.markdown(
        """
        <style>
        :root{--accent:#ff6b6b;--accent-2:#00e5ff;--muted:#d1d5db}
        body {background:linear-gradient(135deg,#0f172a,#0b1020);}
        .brand {display:flex;align-items:center;gap:12px}
        .service-card{background:rgba(255,255,255,0.04);padding:14px;border-radius:10px;margin-bottom:12px}
        .testimonial{padding:12px;border-radius:8px;background:linear-gradient(180deg,rgba(255,255,255,0.02),rgba(255,255,255,0.01));border-left:6px solid var(--accent);}
        .cube{width:160px;height:160px;margin:auto}
        .link{color:var(--accent-2);font-weight:700}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header():
    cols = st.columns([1, 3, 1])
    with cols[0]:
        logo_path = Path('static/img/logo.svg')
        if logo_path.exists():
            st.markdown(f"<img src='{logo_path.as_posix()}' width='160'>", unsafe_allow_html=True)
        else:
            st.markdown("<h2 style='color:linear-gradient(90deg,#ff6b6b,#00e5ff)'>Digital Drift</h2>", unsafe_allow_html=True)
    with cols[1]:
        st.markdown("<h1 style='color:white;margin:0'>Digital Drift — Bold. Vibrant. Modern Marketing.</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#d1d5db;margin:0'>We blend creativity, performance and technology to grow your business online.</p>", unsafe_allow_html=True)
    with cols[2]:
        st.markdown("<div style='text-align:right'><a class='link' href='https://instagram.com/digital_drift26' target='_blank'>@digital_drift26</a><br><a class='link' href='tel:+918847298009'>+91 8847298009</a></div>", unsafe_allow_html=True)


def lead_form(default_service=''):
    with st.form(key=f'lead_form_{default_service}'):
        st.subheader('Get in touch')
        name = st.text_input('Full name')
        email = st.text_input('Email id')
        contact = st.text_input('Contact number')
        submitted = st.form_submit_button('Send')
        if submitted:
            # Basic validation
            if not name or not email or not contact:
                st.error('Please fill all fields.')
            else:
                st.success(f'Thanks {name}, we received your details. We will contact you soon.')
                print('Lead received:', name, email, contact, 'for', default_service)


def render_home():
    st.markdown('<div class="cube">', unsafe_allow_html=True)
    # Show hero and services
    st.markdown('## Next‑gen digital marketing for ambitious brands')
    st.write('We blend creativity, performance and technology to grow your business online.')

    st.markdown('### Our Services')
    # Display services in columns (3 per row)
    svc_items = list(services.items())
    for i in range(0, len(svc_items), 3):
        cols = st.columns(3)
        for idx, (key, svc) in enumerate(svc_items[i:i+3]):
            with cols[idx]:
                st.markdown(f"<div class='service-card'><h4 style='margin:0'>{svc['title']}</h4><p style='color:#d1d5db'>{svc['desc'][:140]}...</p><a class='link' href='#{key}'>Read more</a></div>", unsafe_allow_html=True)

    st.markdown('### Highlighted Work')
    cols = st.columns(len(testimonials))
    for i, t in enumerate(testimonials):
        with cols[i]:
            st.markdown(f"<div class='testimonial'><h4 style='margin:0'>{t['title']}</h4><p style='color:#d1d5db'>&ldquo;{t['quote']}&rdquo;</p><a class='link' href='{t['site']}' target='_blank'>View live</a></div>", unsafe_allow_html=True)


def render_service(slug):
    svc = services.get(slug)
    if not svc:
        st.error('Service not found')
        return
    st.title(svc['title'])
    st.write(svc['desc'])
    st.header('What we do')
    st.write('We tailor strategies based on your business goals. Implementation includes planning, execution, measurement and iterative optimization.')
    st.subheader('Approach')
    st.write('- Discovery & audits\n- Strategy & roadmaps\n- Execution & creative\n- Measurement & optimization')

    st.subheader('Highlighted Testimonials')
    for t in testimonials:
        st.markdown(f"<div class='testimonial' style='margin-bottom:12px'><h4 style='margin:0'>{t['title']}</h4><p style='color:#d1d5db'>&ldquo;{t['quote']}&rdquo;</p><a class='link' href='{t['site']}' target='_blank'>View live</a></div>", unsafe_allow_html=True)


def main():
    st.set_page_config(page_title='Digital Drift', layout='wide')
    render_css()
    render_header()

    # Sidebar navigation and persistent lead form
    st.sidebar.title('Navigate')
    page = st.sidebar.selectbox('Go to', ['Home'] + list(services.keys()))
    st.sidebar.markdown('---')
    st.sidebar.write('Contact us')
    lead_form(default_service=page if page != 'Home' else '')

    # Render selected page
    if page == 'Home':
        render_home()
    else:
        render_service(page)


if __name__ == '__main__':
    main()
