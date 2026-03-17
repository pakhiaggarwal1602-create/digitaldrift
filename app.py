from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = "change-this-secret"

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


@app.route('/')
def home():
    return render_template('home.html', services=services, testimonials=testimonials)


@app.route('/service/<slug>')
def service_page(slug):
    svc = services.get(slug)
    if not svc:
        return redirect(url_for('home'))
    return render_template('service.html', slug=slug, service=svc, testimonials=testimonials)


@app.route('/signup', methods=['POST'])
def signup():
    full_name = request.form.get('full_name', '').strip()
    email = request.form.get('email', '').strip()
    contact = request.form.get('contact', '').strip()
    service = request.form.get('service', '')
    # For now we just flash and print — integrate with CRM/DB when available
    print('Lead received:', full_name, email, contact, 'for', service)
    flash('Thanks {}, we received your details. We will contact you soon.'.format(full_name or 'there'))
    if service:
        return redirect(url_for('service_page', slug=service))
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
