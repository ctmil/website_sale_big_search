# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteSaleBigSearch(http.Controller):
#     @http.route('/website_sale_big_search/website_sale_big_search/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_sale_big_search/website_sale_big_search/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_sale_big_search.listing', {
#             'root': '/website_sale_big_search/website_sale_big_search',
#             'objects': http.request.env['website_sale_big_search.website_sale_big_search'].search([]),
#         })

#     @http.route('/website_sale_big_search/website_sale_big_search/objects/<model("website_sale_big_search.website_sale_big_search"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_sale_big_search.object', {
#             'object': obj
#         })