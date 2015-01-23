// artcrm's admin script

(function (root, $) {
	var appname = 'artcrm';

	function log (text) {
		console.log(appname + ': ' + text);
	}

	$(function () {
		log('Enter')
		log('Exit');
	});

	log('Loaded');
})(window, window.jQuery);