odoo.define('hide_import_ button.hide_import_ button', function (require) {
'use strict';

var Model = require('web.DataModel');
var ListView = require('web.ListView');

ListView.include({
    render_buttons: function() {
        var self = this;
        this._super.apply(this, arguments);
        
        var Users = new Model('res.users');
        Users.call('has_group', ['hide_import_button.show_import_button']).done(function(belongs_to_group) {
        	if (belongs_to_group == false) {
	      		self.$buttons.find('.o_list_button_import').remove();
        	}
	    };
	    
        return this.$buttons;
    },
});

});
