from django.forms import BaseModelForm
from django.forms.models import ModelFormOptions, ALL_FIELDS, fields_for_model
from django.core.exceptions import (
    NON_FIELD_ERRORS,
    FieldError,
    ImproperlyConfigured,
    ValidationError,
)

class KVForm(BaseModelForm):

	def __new__(cls, *args, **kwargs):
		new_obj = super().__new__(cls)
		#TODO
		name = "TODO"
		opts = new_obj._meta = ModelFormOptions(getattr(new_obj, "Meta", None))

		# We check if a string was passed to `fields` or `exclude`,
		# which is likely to be a mistake where the user typed ('foo') instead
		# of ('foo',)
		for opt in ["fields", "exclude", "localized_fields"]:
			value = getattr(opts, opt)
			if isinstance(value, str) and value != ALL_FIELDS:
				msg = (
						"%(model)s.Meta.%(opt)s cannot be a string. "
						"Did you mean to type: ('%(value)s',)?"
						% {
							"model": new_obj.__name__,
							"opt"  : opt,
							"value": value,
						}
				)
				raise TypeError(msg)

		if opts.model:
			# If a model is defined, extract form fields from it.
			if opts.fields is None and opts.exclude is None:
				raise ImproperlyConfigured(
						"Creating a ModelForm without either the 'fields' attribute "
						"or the 'exclude' attribute is prohibited; form %s "
						"needs updating." % name
				)

			if opts.fields == ALL_FIELDS:
				# Sentinel for fields_for_model to indicate "get the list of
				# fields from the model"
				opts.fields = None

			fields = fields_for_model(
					opts.model,
					opts.fields,
					opts.exclude,
					opts.widgets,
					None,
					opts.localized_fields,
					opts.labels,
					opts.help_texts,
					opts.error_messages,
					opts.field_classes,
					# limit_choices_to will be applied during ModelForm.__init__().
					apply_limit_choices_to = False,
			)

			# # make sure opts.fields doesn't specify an invalid field
			# none_model_fields = {k for k, v in fields.items() if not v}
			# missing_fields = none_model_fields.difference(new_obj.declared_fields)
			# if missing_fields:
			# 	message = "Unknown field(s) (%s) specified for %s"
			# 	message = message % (", ".join(missing_fields), opts.model.__name__)
			# 	raise FieldError(message)
			# # Override default model fields with any custom declared ones
			# # (plus, include all the other declared fields).
			# fields.update(new_obj.declared_fields)
		else:
			# fields = new_obj.declared_fields
			# should raise error
			fields = []
			pass

		new_obj.base_fields = fields

		return new_obj
