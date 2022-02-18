(function ($) {
    $(document).ready(function () {
        const $template = $('#id_template').empty();
        $(document).on('change', '#id_customer', function () {
            const _this = $(this);
            $.ajax($ajax_getColletion, {
                method: "POST",
                data: {
                    app_label: 'custodia', model: 'formbox',
                    filters: `{'customer_id': '${_this.val()}'}`
                },
                success: function (response) {
                    $template.empty();
                    $template.append(`<option>---------</option>`)
                    $.each(response, function (i, template) {
                        $template.append(`
                            <option value="${template.id}">${template.name}</option>
                        `)
                    })
                }
            })
        })
    })
})(grp.jQuery)