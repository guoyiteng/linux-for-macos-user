store.set_global_value('hotkey', '<meta>+r')
if re.match('.*(Hyper)', window.get_active_class()):
    logging.debug('terminal refresh buffer')
    engine.set_return_value('<ctrl>+<shift>+r')
else:
    logging.debug('normal')
    engine.set_return_value('<ctrl>+r')
engine.run_script('combo')