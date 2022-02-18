

(function ($) {
    (function () {
        (function () {
            var ajaxQueue;
            ajaxQueue = $({});
            return $.ajaxQueue = function (ajaxOptions) {
                var ajaxComplete;
                ajaxComplete = ajaxOptions.complete;
                return ajaxQueue.queue(function (next) {
                    ajaxOptions.complete = function () {
                        if (ajaxComplete) {
                            ajaxComplete.apply(this, arguments);
                        }
                        return next();
                    };
                    return $.ajax(ajaxOptions);
                });
            };
        })();

    }).call(this);
})(grp.jQuery);

