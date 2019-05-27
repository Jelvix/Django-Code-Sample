!function (a) {
    var b = [], c = [], d = [];
    a.fn.addTag = function (g, h) {
        return h = jQuery.extend({focus: !1, callback: !0}, h), this.each(function () {
            var i = a(this).attr("id"), j = a(this).val().split(e(b[i]));
            if ("" === j[0] && (j = []), g = jQuery.trim(g), c[i].unique && a(this).tagExist(g) || !f(g, c[i], j, b[i])) return a("#" + i + "_tag").addClass("error"), !1;
            if (a("<span>").addClass("tag").append(a("<span>").text(g), a("<a>", {href: "#", class:"glyphicon glyphicon-remove", style:"width:10px; height: 10px;"}).click(function () {
                return a("#" + i).removeTag(encodeURI(g))
            })).insertBefore("#" + i + "_addTag"), j.push(g), a("#" + i + "_tag").val(""), h.focus ? a("#" + i + "_tag").focus() : a("#" + i + "_tag").blur(), a.fn.tagsInput.updateTagsField(this, j), h.callback && d[i] && d[i].onAddTag) {
                var k = d[i].onAddTag;
                k.call(this, this, g)
            }
            if (d[i] && d[i].onChange) {
                var k = (j.length, d[i].onChange);
                k.call(this, this, g)
            }
        }), !1
    }, a.fn.removeTag = function (c) {
        return c = decodeURI(c), this.each(function () {
            var f = a(this).attr("id"), g = a(this).val().split(e(b[f]));
            a("#" + f + "_tagsinput .tag").remove();
            var h = "";
            for (i = 0; i < g.length; ++i) g[i] != c && (h = h + e(b[f]) + g[i]);
            if (a.fn.tagsInput.importTags(this, h), d[f] && d[f].onRemoveTag) {
                d[f].onRemoveTag.call(this, this, c)
            }
        }), !1
    }, a.fn.tagExist = function (c) {
        var d = a(this).attr("id"), f = a(this).val().split(e(b[d]));
        return jQuery.inArray(c, f) >= 0
    }, a.fn.importTags = function (b) {
        var c = a(this).attr("id");
        a("#" + c + "_tagsinput .tag").remove(), a.fn.tagsInput.importTags(this, b)
    }, a.fn.tagsInput = function (f) {
        var i = jQuery.extend({
            interactive: !0,
            placeholder: "Add a tag",
            minChars: 0,
            maxChars: null,
            limit: null,
            validationPattern: null,

            autocomplete: null,
            hide: !0,
            delimiter: ",",
            unique: !0,
            removeWithBackspace: !0
        }, f), j = 0;
        return this.each(function () {
            if (void 0 === a(this).data("tagsinput-init")) {
                a(this).data("tagsinput-init", !0), i.hide && a(this).hide();
                var f = a(this).attr("id");
                f && !e(b[a(this).attr("id")]) || (f = a(this).attr("id", "tags" + (new Date).getTime() + ++j).attr("id"));
                var k = jQuery.extend({
                    pid: f,
                    real_input: "#" + f,
                    holder: "#" + f + "_tagsinput",
                    input_wrapper: "#" + f + "_addTag",
                    fake_input: "#" + f + "_tag"
                }, i);
                b[f] = k.delimiter, c[f] = {
                    minChars: i.minChars,
                    maxChars: i.maxChars,
                    limit: i.limit,
                    validationPattern: i.validationPattern,
                    unique: i.unique
                }, (i.onAddTag || i.onRemoveTag || i.onChange) && (d[f] = [], d[f].onAddTag = i.onAddTag, d[f].onRemoveTag = i.onRemoveTag, d[f].onChange = i.onChange);
                var l = '<div id="' + f + '_tagsinput" class="tagsinput"><div id="' + f + '_addTag">';
                i.interactive && (l = l + '<input id="' + f + '_tag" value="" placeholder="' + i.placeholder + '">'), a(l).insertAfter(this), a(k.holder).css("min-height", i.height), "" !== a(k.real_input).val() && a.fn.tagsInput.importTags(a(k.real_input), a(k.real_input).val()), i.interactive && (a(k.fake_input).val(""), a(k.fake_input).data("pasted", !1), a(k.fake_input).on("focus", k, function (b) {
                    a(k.holder).addClass("focus"), "" === a(this).val() && a(this).removeClass("error")
                }), a(k.fake_input).on("blur", k, function (b) {
                    a(k.holder).removeClass("focus")
                }), null !== i.autocomplete && void 0 !== jQuery.ui.autocomplete ? (a(k.fake_input).autocomplete(i.autocomplete), a(k.fake_input).on("autocompleteselect", k, function (b, c) {
                    return a(b.data.real_input).addTag(c.item.value, {focus: !0, unique: i.unique}), !1
                }), a(k.fake_input).on("keypress", k, function (b) {
                    g(b) && a(this).autocomplete("close")
                })) : a(k.fake_input).on("blur", k, function (b) {
                    return a(b.data.real_input).addTag(a(b.data.fake_input).val(), {focus: !0, unique: i.unique}), !1
                }), a(k.fake_input).on("keypress", k, function (b) {
                    if (g(b)) return b.preventDefault(), a(b.data.real_input).addTag(a(b.data.fake_input).val(), {
                        focus: !0,
                        unique: i.unique
                    }), !1
                }), a(k.fake_input).on("paste", function () {
                    a(this).data("pasted", !0)
                }), a(k.fake_input).on("input", k, function (b) {
                    if (a(this).data("pasted")) {
                        a(this).data("pasted", !1);
                        var c = a(b.data.fake_input).val();
                        c = c.replace(/\n/g, ""), c = c.replace(/\s/g, "");
                        var d = h(b.data.delimiter, c);
                        if (d.length > 1) {
                            for (var e = 0; e < d.length; ++e) a(b.data.real_input).addTag(d[e], {
                                focus: !0,
                                unique: i.unique
                            });
                            return !1
                        }
                    }
                }), k.removeWithBackspace && a(k.fake_input).on("keydown", function (b) {
                    if (8 == b.keyCode && "" === a(this).val()) {
                        b.preventDefault();
                        var c = a(this).closest(".tagsinput").find(".tag:last > span").text(),
                            d = a(this).attr("id").replace(/_tag$/, "");
                        a("#" + d).removeTag(encodeURI(c)), a(this).trigger("focus")
                    }
                }), a(k.fake_input).keydown(function (b) {
                    -1 === jQuery.inArray(b.keyCode, [13, 37, 38, 39, 40, 27, 16, 17, 18, 225]) && a(this).removeClass("error")
                }))
            }
        }), this
    }, a.fn.tagsInput.updateTagsField = function (c, d) {
        var f = a(c).attr("id");
        a(c).val(d.join(e(b[f])))
    }, a.fn.tagsInput.importTags = function (c, e) {
        a(c).val("");
        var f = a(c).attr("id"), g = h(b[f], e);
        for (i = 0; i < g.length; ++i) a(c).addTag(g[i], {focus: !1, callback: !1});
        if (d[f] && d[f].onChange) {
            d[f].onChange.call(c, c, g)
        }
    };
    var e = function (a) {
        return void 0 === a ? a : "string" == typeof a ? a : a[0]
    }, f = function (b, c, d, e) {
        var f = !0;
        return "" === b && (f = !1), b.length < c.minChars && (f = !1), null !== c.maxChars && b.length > c.maxChars && (f = !1), null !== c.limit && d.length >= c.limit && (f = !1), null === c.validationPattern || c.validationPattern.test(b) || (f = !1), "string" == typeof e ? b.indexOf(e) > -1 && (f = !1) : a.each(e, function (a, c) {
            return b.indexOf(c) > -1 && (f = !1), !1
        }), f
    }, g = function (b) {
        var c = !1;
        return 13 === b.which || ("string" == typeof b.data.delimiter ? b.which === b.data.delimiter.charCodeAt(0) && (c = !0) : a.each(b.data.delimiter, function (a, d) {
            b.which === d.charCodeAt(0) && (c = !0)
        }), c)
    }, h = function (b, c) {
        if ("" === c) return [];
        if ("string" == typeof b) return c.split(b);
        var d = c;
        return a.each(b, function (a, b) {
            d = d.split(b).join("∞")
        }), d.split("∞")
    }
}(jQuery);