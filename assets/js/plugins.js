$(document).ready(function() {
    $('.datetimepicker, .datepicker').each(function() {
        $(this).datetimepicker({
            lang: 'fr',
            i18n: {
                fr: {
                    months: ['Janvier', 'Février', 'Mars', 'Avril',
                        'Mai', 'Juin', 'Juillet', 'Août',
                        'Septembre', 'Octobre', 'Novembre', 'Décembre'],
                    dayOfWeek: ['Dim', 'Lun', 'Mar', 'Mer',
                        'Jeu', 'Ven', 'Sam']
                }
            },
            timepicker: $(this).hasClass('datetimepicker'),
            format: 'Y-m-d' + ($(this).hasClass('datetimepicker') ? ' H:i' : ''),
            allowBlank: $(this).data('datetimepicker-allowblank') ? true : false
        });
    });

    $('textarea.ckeditor:not(.readonly)').ckeditor({
        customConfig: '/assets/js/cke_config.js'
    });
    
    $('form').submit(function() {
        $('button.disable-on-submit', this).each(function() {
            $(this).prop('disabled', true);
        });
    });
    
    $('.tablesorter').tablesorter();
});

String.prototype.ucfirst = function() {
    var string = this.split('');
    string[0] = string[0].toUpperCase();
    return string.join('');
};
